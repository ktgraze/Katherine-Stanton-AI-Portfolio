# EduBot: Educational Chatbot
### ITAI 2373 - Natural Language Processing | Houston City College

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-TF--IDF-orange)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)

---

## Problem Statement

Educational institutions generate large amounts of student performance data, but this data is rarely accessible to students or educators in a conversational format. EduBot addresses this by transforming a structured student performance dataset into a retrieval-based chatbot that answers natural language questions about factors affecting academic outcomes — including test preparation, lunch type, parental education, and gender-based performance differences.

---

## Approach and Methodology

EduBot is a retrieval-based chatbot built using TF-IDF vectorization and cosine similarity matching. The pipeline consists of the following stages:

**1. Data Loading and Exploration**
The Students Performance in Exams dataset (CSV) is loaded using Pandas. Basic statistics, missing value checks, and grouped comparisons are performed to extract meaningful insights from the data.

**2. Knowledge Base Construction**
Eight factual sentences summarizing key findings from the dataset are manually curated into a knowledge base. This transforms a numeric dataset into a form suitable for text-based retrieval.

**3. TF-IDF Vectorization**
Scikit-learn's TfidfVectorizer fits and transforms the knowledge base sentences into a TF-IDF matrix, representing each sentence as a weighted vector of term importance.

**4. Cosine Similarity Matching**
When a user submits a question, it is vectorized and compared against the knowledge base using cosine similarity. The most similar sentence is returned as the chatbot's response. A confidence threshold of 0.2 is applied — queries below this threshold receive a graceful fallback response.

**5. Chatbot Interface**
Two chat loop implementations are provided: a basic version and an enhanced version with improved formatting and user experience elements including greetings, exit handling, and clear instructions.

---

## Results and Evaluation

The chatbot successfully retrieves relevant responses to questions about student performance factors including test preparation, gender differences, lunch type, parental education level, and score correlations. The confidence threshold prevents the chatbot from returning irrelevant matches on out-of-scope queries. Sample questions and outputs are included directly in the notebook for demonstration.

---

## Data Sources

- **Students Performance in Exams Dataset** — Kaggle  
  SPS. (2018). *Students Performance in Exams*. Retrieved April 2025, from https://www.kaggle.com/datasets/spscientist/students-performance-in-exams  
  The dataset contains 1,000 records of student exam scores across math, reading, and writing, along with demographic and preparatory factors.

---

## Requirements and Dependencies

See `requirements.txt` for the full dependency list. Key libraries:

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and analysis |
| `numpy` | Numerical operations |
| `nltk` | Natural language processing utilities |
| `scikit-learn` | TF-IDF vectorization and cosine similarity |
| `matplotlib` | Data visualization |
| `seaborn` | Statistical data visualization |

To run the notebook:

```bash
pip install -r requirements.txt
jupyter notebook Team6_EducationSector_MidtermProject_EduBotChatBox_ITAI2373.ipynb
```

Or open directly in Google Colab and run all cells in order.

---

## Learning Outcomes

Working on this project introduced our team to the fundamentals of retrieval-based NLP systems and the practical challenges of adapting structured data for conversational use. Building the knowledge base manually from dataset insights highlighted how much domain understanding is required before any NLP model can perform well. Implementing TF-IDF vectorization and cosine similarity gave hands-on experience with core text representation techniques and their limitations compared to semantic models. Setting a confidence threshold for graceful fallback responses reinforced the importance of designing for edge cases in user-facing AI systems.

---

## Team Information

**Course:** ITAI 2373 - Natural Language Processing
**Institution:** Houston City College
**Semester:** Spring 2025

**Team Members**
- Natalia Solorzano
- **Katherine Stanton**
- Jaya Verma
- Mustafa Yucedag
- Ali Safdar Zaidi

---

## References

1. SPS. (2018). *Students Performance in Exams Dataset*. Kaggle. https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
2. Oracle. (n.d.). *What is a chatbot?* https://www.oracle.com/chatbots/what-is-a-chatbot
3. Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830. https://scikit-learn.org
4. The pandas development team. (2020). *Pandas Documentation*. https://pandas.pydata.org
5. Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O'Reilly Media.
6. Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering*, 9(3), 90–95. https://matplotlib.org
7. Waskom, M. L. (2021). Seaborn: Statistical data visualization. *Journal of Open Source Software*, 6(60), 3021. https://seaborn.pydata.org
