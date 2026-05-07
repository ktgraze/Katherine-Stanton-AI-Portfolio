# Define the content of app.py
app_code = """
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

# Streamlit UI
st.title("Credit Card Fraud Detection App")
st.write("Enter transaction details below:")

# User inputs
time = st.number_input("Transaction Time (seconds)", min_value=0, step=1)
amount = st.number_input("Transaction Amount ($)", min_value=0.0, format="%.2f")

# Simulating PCA-transformed features (as actual PCA values are unknown here)
pca_features = np.random.randn(28)  # Adjust this to match your real feature set

# Prepare input data
input_data = np.hstack(([time, amount], pca_features)).reshape(1, -1)

# Predict fraud
if st.button("Check Fraud"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Safe.")
"""

# Write the app code to a Python file (app.py)
with open("app.py", "w") as f:
    f.write(app_code)

# Provide a download link for the app.py
from google.colab import files
files.download("app.py")
