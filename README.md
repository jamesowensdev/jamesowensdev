<div align="center">

# Hi there, I'm James Owens 👋

### PhD Researcher | Computational Ecology | Geographic Profiling
**School of Biological Sciences @ Queen's University Belfast**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/) 
[![Email](https://img.shields.io/badge/Email-Contact_Me-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@qub.ac.uk)
[![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)](https://www.r-project.org/)

---

</div>

## 🔭 Current Research Focus

I am analysing the efficacy of **Geographic Profiling (GP)** techniques in predicting the nesting sites of **Central Place Foragers (CPF)**. My work focuses on variable, human-dominated landscapes where traditional detection methods struggle.

To solve this, I build stochastic **Agent-Based Models (ABM)** to simulate animal movement and optimize camera trap networks.

## 🧬 Featured Project: CPF & Camera Trap Simulation

My current work involves developing a stochastic simulation engine in **R** (`R6`, `terra`, `gganimate`) to model how camera trap placement affects detection probability.

> **The Model:** A Correlated Random Walk (CRW) observed by a probabilistic sensor network.

<div align="center">
  <img src="https://github.com/jamesowensdev/cpf_simulation/blob/main/readme_assets/simulation_gifs/README_Example_Run.gif?raw=true" width="600" />
</div>

<br/>

<details>
<summary><b>📐 See the Mathematical Logic (Click to Expand)</b></summary>

I model detection probability not as a binary radius, but as a **Reverse Sigmoid Function** to mimic real-world sensor decay:

$$P(d) = P_{max} \times \frac{1}{1 + e^{k \cdot (d - d_{inf})}}$$

Where:
* $P_{max}$ is the maximum probability at the lens.
* $k$ controls the steepness of the probability decay.
* $d_{inf}$ is the distance at which probability drops to 50%.

</details>

## 🛠️ Technical Stack

* **Languages:** R (Advanced), Python, SQL
* **Modelling:** Agent-Based Modelling (ABM), Stochastic Simulation, R6 OOP
* **Spatial:** GIS (`terra`, `sf`), Spatial Ecology
* **Tools:** Git, Quarto, LaTeX, Docker

## 📊 GitHub Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=jamesowensdev&show_icons=true&theme=radical" height="150" alt="stats graph"  />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=jamesowensdev&layout=compact&theme=radical" height="150" alt="languages graph" />
</div>

---
<div align="center">
  <small><i>"All models are wrong, but some are useful." — George Box</i></small>
</div>
<!---
jamesowensdev/jamesowensdev is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
