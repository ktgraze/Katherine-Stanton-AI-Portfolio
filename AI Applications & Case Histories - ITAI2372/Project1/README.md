# Credit Card Fraud Detection
### ITAI 2372 - AI Applications & Case Histories | Houston City College

![Python](https://img.shields.io/badge/Python-3.x-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-best%20model-green)
![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red)
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ktgraze/Mod4ITAI2372/blob/main/CreditCardFraudDetection.ipynb)

---

## Live Demo

The trained XGBoost model is deployed as an interactive Streamlit application:

**https://mod4itai2372-n7m64fpxnshozp65pbvsc8.streamlit.app/#credit-card-fraud-detection-app**

![Home Screen](https://github.com/user-attachments/assets/98afc363-ee1a-49d5-85a1-0c56be603efc)
![Testing the Application](https://github.com/user-attachments/assets/6fd4c287-7571-46a5-9506-66bf656899b8)

---

## Problem Statement

Credit card fraud is a costly and prevalent problem that causes significant financial harm to consumers and institutions alike. Fraud detection is a particularly challenging machine learning problem due to extreme class imbalance — legitimate transactions vastly outnumber fraudulent ones, making it easy for models to achieve high accuracy while still missing most actual fraud cases. This project explores multiple approaches to handling this imbalance and identifies the best-performing model for deployment in a real-time fraud detection application.

---

## Approach and Methodology

The project follows an end-to-end machine learning pipeline across the following stages:

**1. Data Exploration and Visualization**
The dataset is loaded and explored using Pandas and Seaborn. Class distribution, transaction amount distribution, and PCA component scatter plots are generated to understand the imbalance and feature structure.

**2. Preprocessing**
Features are scaled using StandardScaler. The dataset is split into training and test sets using an 80/20 stratified split to preserve the fraud-to-legitimate ratio.

**3. Model Experimentation**
Four approaches are trained and evaluated:
- Logistic Regression (baseline)
- Logistic Regression with class_weight="balanced"
- SMOTE (Synthetic Minority Over-sampling) combined with RandomUnderSampler
- XGBoost with scale_pos_weight to handle imbalance natively
- IsolationForest as an unsupervised anomaly detection baseline

**4. Model Selection and Saving**
XGBoost is selected as the best performing model based on its balance of fraud recall and false positive rate. The model is saved using joblib for deployment.

**5. Streamlit Deployment**
A simple UI is built with Streamlit, allowing users to input transaction features and receive a real-time fraud prediction from the saved XGBoost model.

---

## Results and Evaluation

| Model | Fraud Recall | False Positives | Notes |
|-------|-------------|-----------------|-------|
| Logistic Regression (baseline) | 64% | 13 | High accuracy, misleading due to imbalance |
| Logistic Regression (balanced) | 92% | 1,390 | Better recall, far too many false alarms |
| XGBoost | High | 10 | Best balance of recall and precision |
| IsolationForest | Lower than XGBoost | 553 | Unsupervised — weakest overall performance |

XGBoost significantly outperformed all other models, detecting more fraud cases than the baseline Logistic Regression while producing far fewer false positives than the balanced Logistic Regression model.

---

## Data Sources

**Credit Card Fraud Detection Dataset** — Kaggle, Machine Learning Group - ULB

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The dataset contains 284,807 credit card transactions made by European cardholders in September 2013, of which 492 (0.17%) are fraudulent. Features V1 through V28 are anonymized PCA components. Additional features include Time, Amount, and Class (0 = legitimate, 1 = fraud).

---

## Requirements and Dependencies

See `requirements.txt` for the full dependency list. Key libraries:

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and exploration |
| `scikit-learn` | Preprocessing, Logistic Regression, IsolationForest |
| `xgboost` | Best-performing fraud detection model |
| `imbalanced-learn` | SMOTE and RandomUnderSampler |
| `joblib` | Model serialization |
| `matplotlib` | Data visualization |
| `seaborn` | Statistical visualization |
| `streamlit` | Deployed UI |
| `kaggle` | Dataset download via Kaggle API |

To run the notebook locally:

```bash
pip install -r requirements.txt
jupyter notebook CreditCardFraudDetection.ipynb
```

Or open directly in Google Colab using the badge above. A Kaggle API key (`kaggle.json`) is required to download the dataset.

---

## Learning Outcomes

This project deepened my understanding of the practical challenges of working with highly imbalanced datasets in a real-world machine learning context. Experimenting with multiple approaches — from class weighting to oversampling to gradient boosting — made clear that accuracy alone is a misleading metric when class imbalance is severe, and that the right evaluation metric depends heavily on the cost of each type of error. Selecting XGBoost as the final model reinforced how ensemble methods and built-in imbalance handling can outperform traditional approaches with less preprocessing overhead. Deploying the model as a Streamlit application provided practical experience connecting a trained model to a user-facing interface.

---
