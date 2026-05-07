# 🩺 TriagePal: AI Multi-Modal Healthcare Triage Agent  

[![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)](https://itai-2277capstoneprojecttriagepalhealthcareagent-bl9hwtxu9uskl.streamlit.app/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red)](https://streamlit.io/)
[![Model](https://img.shields.io/badge/Model-CNN%20%2B%20BioBERT%20%2B%20RandomForest-blue)]()

---

## ✨ Live Demo

The TriagePal agent is deployed on **Streamlit Community Cloud** and ready for real-time interaction.

👉 **Try the live app here:**  
### https://itai-2277capstoneprojecttriagepalhealthcareagent-bl9hwtxu9uskl.streamlit.app/

## Screenshots

### Home Screen - Upload Interface
![Home Screen](/images/Home%20Screen.png)

### Analysis Results - Summary & Report
![Results Screen](/images/Results%20Screen.png)

### Recent Analyses Table
![Recent Analyses](/images/Recent%20Analyses.png)

---

## 🎯 Project Overview (ITAI-2277 Capstone)

TriagePal is the **Phase 4 Integrated System Prototype** for the *AI Applications and Resources (ITAI-2277)* course at **Houston City College**.

It is designed to provide a **preliminary, AI-supported triage score** using both:

- 🖼️ **Image analysis** via a CNN  
- 📝 **Symptom text analysis** using BioBERT NLP  
- 🌲 **Random Forest meta-classifier** to integrate both modalities  

### 🧠 How It Works
The system uses a multi-step intelligence pipeline:

1. **Computer Vision (CV)**  
   A TensorFlow CNN model analyzes an uploaded eye image to detect signs of infection.

2. **Natural Language Processing (NLP)**  
   A BioBERT model extracts symptoms and severity indicators from the user’s text.

3. **Triage Integration**  
   A Random Forest classifier combines:
   - CNN prediction  
   - Symptom count  
   - NLP-derived urgency score  
   
   → Producing a **Low, Medium, or High urgency** triage label.

---

## ⚙️ Technology Stack

| Component | Technology / Model | Purpose |
|----------|--------------------|---------|
| **User Interface** | Streamlit | Provides the interactive web app |
| **Image Model** | TensorFlow CNN (`triagepal_optimized_model.h5`) | Predicts condition from image |
| **NLP Model** | BioBERT (`dmis-lab/biobert-v1.1`) | Extracts symptoms and urgency |
| **Triage Logic** | Scikit-learn Random Forest (`rf_triage_agent.pkl`) | Final urgency classification |
| **Database** | SQLite (`triagepal.db`) | Stores session reports |
| **Deployment** | Streamlit Cloud + GitHub | Hosts the live application |

### **Best Model Performance (Phase 3 Evaluation)**  
- **Test Accuracy:** 0.9307  
- **ROC–AUC:** 0.9870  

---

## 📁 Repository Structure
```plaintext
📦 ITAI-2277_CapstoneProject_TriagePalHealthcareAgent
├── app.py # Streamlit interface
├── requirements.txt # Dependency list
├── triagepal.db # SQLite database for saved evaluations
└── models/
├── triagepal_optimized_model.h5 # CNN model weights
└── rf_triage_agent.pkl # Random Forest triage model
```

---

## 🚀 Setup for Local Development

### 1. Clone the Repository
```bash
git clone https://github.com/ktgraze/ITAI-2277_CapstoneProject_TriagePalHealthcareAgent.git
cd ITAI-2277_CapstoneProject_TriagePalHealthcareAgent
```

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the App
streamlit run app.py

## 🧑‍💻 Team Information

**Course:** ITAI-2277 — AI Applications and Resources
**Institution:** Houston City College

**Team Members**

- Jazmine Brown

- Javon Darby

- Jeffery Dirden
  
- **Katherine Stanton**
