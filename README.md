<div align="center">

# Hi there, I'm James Owens 👋

### PhD Researcher | Computational Ecology | Statistical Ecology | Spatial Ecology 
**School of Biological Sciences @ Queen's University Belfast**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/james-owens-91b731168) 
[![Email](https://img.shields.io/badge/Email-Contact_Me-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jowens24@qub.ac.uk)
[![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)](https://www.r-project.org/)

---

</div>

## 🔭 Current Research Focus

I am analysing the efficacy of **Geographic Profiling (GP)** techniques in predicting the nesting sites of **Central Place Foragers (CPF)**. My work focuses on analysing current methods and their shortcomings when applied to ecological processes, and will in future lead to the development and fine-tuning of a bespoke Ecological Geographic Profiling model.

To begin with, I am building stochastic **Agent-Based Models (ABM)** to simulate animal movement and generate datasets to apply current GP methods to. Simultaneously I am investigating best sampling practices, using highlighting methods with non-perfect detection, and informing how studies should be setup in future to make the most out of GP methods.

## 🧬 Featured Project: CPF & Camera Trap Simulation

My current work involves developing a stochastic simulation engine in **R** (`R6`, `terra`, `gganimate`) to model how camera trap placement affects detection probability.

This is the first bulding block in being able to effectively and reproducibly apply GP methods to simulated datasets.

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

* **Languages:** R, Java, SQL, Python, C, Rust (Beginner)
* **Modelling:** Agent-Based Modelling (ABM), Stochastic Simulation, R6 OOP
* **Spatial:** GIS (`terra`, `sf`), Spatial Ecology
* **Tools:** Git, Quarto, LaTeX, Docker
