"""Builds assets/languages.svg: the share of each programming language across my repositories.

Counts bytes of code as GitHub reports them, over every repository I own (public and
private, forks excluded), and publishes only the aggregate percentages.

Needs a token in GH_TOKEN with read access to my repositories. Run from the repository root:

  GH_TOKEN=$(gh auth token) python scripts/language_stats.py
"""

import json
import os
import urllib.request
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

OWNER = "jamesowensdev"
EXCLUDE = {"HTML", "CSS", "Dockerfile"}  # generated or markup output rather than code I write
MIN_SHARE = 1.5  # smaller languages are pooled into "Other"
MAX_ROWS = 7
OUT = Path(__file__).resolve().parents[1] / "assets" / "languages.svg"

COLOURS = {
  "Python": "#3572A5", "TypeScript": "#3178C6", "R": "#198CE7", "Lua": "#4A5BD1", "Java": "#B07219",
  "Rust": "#DEA584", "JavaScript": "#F1E05A", "Svelte": "#FF3E00", "SQL": "#E38C00", "C": "#7A7A7A",
}


def api(path: str):
  request = urllib.request.Request(
    "https://api.github.com" + path,
    headers={"Authorization": "Bearer " + os.environ["GH_TOKEN"], "Accept": "application/vnd.github+json"},
  )
  with urllib.request.urlopen(request) as response:
    return json.load(response)


def repositories() -> list[str]:
  names, page = [], 1
  while True:
    batch = api(f"/user/repos?affiliation=owner&per_page=100&page={page}")
    names += [r["name"] for r in batch if not r["fork"] and r["owner"]["login"] == OWNER]
    if len(batch) < 100:
      return names
    page += 1


def totals() -> Counter:
  counts: Counter = Counter()
  for name in repositories():
    counts.update(api(f"/repos/{OWNER}/{name}/languages"))
  return Counter({k: v for k, v in counts.items() if k not in EXCLUDE})


def shares(counts: Counter) -> list[tuple[str, float]]:
  total = sum(counts.values())
  rows = [(k, 100 * v / total) for k, v in counts.most_common()]
  kept = [r for r in rows if r[1] >= MIN_SHARE][:MAX_ROWS]
  other = 100 - sum(share for _, share in kept)
  return kept + ([("Other", other)] if other > 0.05 else [])


def render(rows: list[tuple[str, float]]) -> str:
  width, row_h, top, label_w, bar_w = 520, 28, 64, 92, 340
  height = top + row_h * len(rows) + 30
  lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Programming languages by share of code">',
    "<style>",
    "  text { font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: #24292f; }",
    "  .muted { fill: #57606a; } .track { fill: #d0d7de; opacity: 0.45; }",
    "  @media (prefers-color-scheme: dark) { text { fill: #e6edf3; } .muted { fill: #8b949e; } .track { fill: #6e7681; opacity: 0.35; } }",
    "</style>",
    '<text x="0" y="22" font-size="17" font-weight="600">Languages across my repositories</text>',
    '<text x="0" y="42" font-size="12" class="muted">Share of code by size, public and private repositories. HTML, CSS and Dockerfile excluded.</text>',
  ]
  for i, (name, share) in enumerate(rows):
    y = top + i * row_h
    colour = COLOURS.get(name, "#8b949e")
    fill = max(share / rows[0][1] * bar_w, 3)
    lines += [
      f'<text x="0" y="{y + 14}" font-size="13">{escape(name)}</text>',
      f'<rect class="track" x="{label_w}" y="{y + 3}" width="{bar_w}" height="14" rx="7"/>',
      f'<rect x="{label_w}" y="{y + 3}" width="{fill:.1f}" height="14" rx="7" fill="{colour}"/>',
      f'<text x="{label_w + bar_w + 12}" y="{y + 14}" font-size="13" class="muted">{share:.1f}%</text>',
    ]
  lines.append("</svg>")
  return "\n".join(lines) + "\n"


if __name__ == "__main__":
  rows = shares(totals())
  OUT.parent.mkdir(exist_ok=True)
  OUT.write_text(render(rows), encoding="utf-8")
  for name, share in rows:
    print(f"{name:<12}{share:5.1f}%")
