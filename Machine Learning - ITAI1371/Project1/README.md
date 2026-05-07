# The Classic Iris Dataset: Multiclass Classification
### Machine Learning | Houston City College

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Platform](https://img.shields.io/badge/Platform-Google%20Colab-lightgrey)

---

## Note on Context

This notebook represents work from my first AI course involving code. It is included in this portfolio not as a showcase of technical sophistication, but as an honest record of where my machine learning journey began. The skills demonstrated here — data exploration, baseline modeling, and classification — form the foundation that later projects such as the Houston Railroad Crossing Blockage Prediction Agent and the Credit Card Fraud Detection app were built upon.

---

## Problem Statement

Given four measurements of an iris flower — sepal length, sepal width, petal length, and petal width — predict which of three species the flower belongs to: Setosa, Versicolor, or Virginica. This is a multiclass classification problem and one of the most well-known introductory datasets in machine learning.

---

## Approach and Methodology

**1. Data Loading and Exploration**
The Iris dataset is loaded using scikit-learn's built-in datasets module. Basic descriptive statistics are computed and the structure of the dataset is explored using Pandas.

**2. Exploratory Data Analysis**
Histograms are plotted for each of the four features. Relationship plots are generated to visualize how each feature correlates with the target species. A pairplot provides a comprehensive view of feature interactions across all three classes.

**3. Baseline Model**
Before training any model, a baseline accuracy of 33% is established — the expected accuracy of randomly guessing among three equally balanced classes. All models are expected to exceed this threshold.

**4. Manual Rule-Based Model**
A simple hand-crafted classifier using petal length cutoff values is implemented to demonstrate the concept of classification before introducing library-based models.

**5. Logistic Regression**
A Logistic Regression model is trained using scikit-learn on a 75/25 train/validation split. Model accuracy is evaluated on the validation set.

**6. K-Nearest Neighbors**
A KNeighborsClassifier with k=12 is introduced and fit to the training data.

---

## Results and Evaluation

- **Baseline accuracy:** 33% (random chance across three classes)
- **Manual rule-based model:** Achieves reasonable accuracy using petal length cutoffs alone, demonstrating that even simple rules can outperform random chance significantly
- **Logistic Regression:** Trained and evaluated on a validation split; accuracy recorded during the session

Note: This notebook reflects early-stage work and does not include a full final evaluation or model comparison summary.

---

## Data Sources

The Iris dataset is built into scikit-learn and requires no external download:

```python
from sklearn import datasets
data = datasets.load_iris()
```

It contains 150 samples across three iris species with four features each: sepal length, sepal width, petal length, and petal width.

---

## Requirements and Dependencies

See `requirements.txt` for the full dependency list. Key libraries:

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `matplotlib` | Feature distribution visualization |
| `seaborn` | Relational and pairplot visualizations |
| `scikit-learn` | Dataset, train/test split, Logistic Regression, KNN |

To run the notebook:

```bash
pip install -r requirements.txt
jupyter notebook The_Classic_Iris_Dataset.ipynb
```

---

## Learning Outcomes

This was my introduction to the end-to-end machine learning workflow. Working through this notebook for the first time taught me how to frame a prediction problem, explore data visually before modeling, establish a meaningful baseline, and evaluate a model's performance honestly. It also introduced me to the importance of separating training and validation data — a principle that became foundational in every subsequent project I built in this program.

---
