# SLAM: Simultaneous Localization and Mapping
### ITAI — Robot Operating System & Platforms | Houston City College

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![GTSAM](https://img.shields.io/badge/GTSAM-Factor%20Graphs-orange)](https://gtsam.org/)
[![Platform](https://img.shields.io/badge/Platform-Google%20Colab-yellow)](https://colab.research.google.com/)

---

## Problem Statement

One of the fundamental challenges in robotics is enabling a robot to navigate an unknown environment without prior knowledge of its location or a pre-existing map. SLAM (Simultaneous Localization and Mapping) addresses this chicken-and-egg problem: localization requires a map, and mapping requires knowing where you are. This lab explores how factor graphs and probabilistic optimization can solve both problems simultaneously, even in the presence of noisy sensor data.

---

## Approach and Methodology

This lab implements SLAM using **GTSAM** (Georgia Tech Smoothing and Mapping), an open-source C++ library with Python bindings that models SLAM problems as factor graphs and solves them via nonlinear optimization.

The lab progresses through three stages of increasing complexity:

**1. Pose SLAM with Loop Closure**
A simple five-pose factor graph is constructed using odometry (Between) factors and a loop closure constraint. The **Gauss-Newton optimizer** refines pose estimates by iteratively minimizing total error across the graph.

**2. Landmark SLAM with Range-Bearing Measurements**
Two landmarks are introduced into the factor graph using bearing-range measurements. The **Levenberg-Marquardt optimizer** is used here for its robustness to poor initial estimates and nonlinear noise.

**3. Large-Scale Real-World SLAM**
A realistic SLAM example is loaded from GTSAM's built-in `example.graph` dataset, representing a robot traversing a complex environment. The Levenberg-Marquardt optimizer refines the trajectory, and initial vs. optimized paths are visualized interactively using Plotly.

---

## Results and Evaluation

- **Pose SLAM**: The Gauss-Newton optimizer successfully converged on a consistent robot trajectory, with marginal covariance ellipses showing uncertainty at each pose.
- **Landmark SLAM**: The Levenberg-Marquardt optimizer correctly localized two landmarks relative to three robot poses using noisy bearing-range measurements.
- **Large-Scale SLAM**: The optimized trajectory visibly corrected accumulated drift compared to the initial noisy estimate, demonstrating the effectiveness of loop closures and constraint-based optimization at scale.

---

## Data Sources

The large-scale SLAM example uses `example.graph`, a built-in example dataset included with the GTSAM library. No external dataset download is required — the file is accessed automatically via `gtsam.findExampleDataFile('example.graph')`.

---

## Requirements and Dependencies

See `requirements.txt` for the full dependency list. Key libraries:

| Library | Purpose |
|---------|---------|
| `gtsam` | Factor graph construction and optimization |
| `gtbook` | Course display utilities |
| `numpy` | Numerical operations |
| `matplotlib` | Static trajectory and covariance visualization |
| `plotly` | Interactive trajectory visualization |

---

## How to Run

### Option 1 — Google Colab (Recommended)
1. Open `Stanton_Lab_10_SLAM.ipynb` in Google Colab
2. Run all cells from top to bottom in order
3. The `%pip install -q gtbook` cell will install all required dependencies automatically

### Option 2 — Local Jupyter
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Launch Jupyter:
```bash
jupyter notebook Stanton_Lab_10_SLAM.ipynb
```
3. Run all cells in order

> **Note:** GTSAM requires a C++ build environment for local installation. Google Colab is strongly recommended to avoid setup complexity.

---

## Learning Outcomes

This lab deepened my understanding of how probabilistic robotics handles the fundamental tension between localization and mapping. Implementing factor graphs in GTSAM made abstract concepts like odometry noise, loop closure, and marginal covariance tangible and visual. Comparing the Gauss-Newton and Levenberg-Marquardt optimizers highlighted important practical trade-offs in nonlinear optimization — particularly how initial estimate quality affects convergence. Working with the large-scale real-world dataset reinforced how SLAM scales from toy examples to realistic robot navigation scenarios.

---

