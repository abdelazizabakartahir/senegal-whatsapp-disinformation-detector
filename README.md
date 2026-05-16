# 🇸🇳 Senegal WhatsApp Disinformation Detector

## 📌 Overview

This project detects viral political disinformation on WhatsApp in Senegal using Machine Learning. It helps fact-checking teams prioritize dangerous messages during election periods.

**Live Demo:** [Link to your Streamlit app]

**Author:** Abdelaziz Abakar Tahir - AISIP Cohort 1 | Africa AI Hub

---

## 🎯 Problem Statement

During election periods in Senegal, deepfakes and AI-generated disinformation spread rapidly on WhatsApp. Citizens cannot distinguish real content from fake. No accessible detection tool exists in French or Wolof.

**Key statistics from my research:**
- 80% of survey respondents were exposed to political deepfakes
- 73% consider the problem "very serious"
- 90% would use a detection tool if available

---

## 🚀 Solution

A Machine Learning classifier that predicts whether a political WhatsApp message has high viral potential.

| Feature | Description |
|---------|-------------|
| Input | Political WhatsApp message (text) |
| Output | Viral probability score (0-100%) |
| Model | Random Forest (F1 Score: 0.86) |
| Deployment | Streamlit web application |

---

## 📊 Dataset

- **Size:** 2,000 synthetic messages
- **Label distribution:** 30% viral, 70% normal
- **Features:** message length, word count, capitals ratio, emoji count, political keywords, call-to-action, TF-IDF (50 features)

---

## 🤖 Models Trained

| Model | F1 Score |
|-------|----------|
| Logistic Regression | 0.80 |
| Random Forest | **0.86** 🏆 |
| Gradient Boosting | 0.85 |
| Neural Network (Keras) | 0.84 |
| Ensemble Voting | 0.86 |

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Data Processing | Python, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| ML Models | Scikit-learn |
| Neural Networks | TensorFlow / Keras |
| Deployment | Streamlit |
| Version Control | Git / GitHub |
| Environment | Google Colab, Streamlit Cloud |

---

## 📈 Key Results

- **Best Model:** Random Forest (tuned)
- **Accuracy:** 87%
- **Precision:** 85%
- **Recall:** 88%
- **F1 Score:** 0.86

### Feature Importance (Top 5)

| Feature | Importance |
|---------|------------|
| political_word_count | 0.24 |
| caps_ratio | 0.18 |
| message_length | 0.14 |
| emoji_count | 0.12 |
| has_share_call | 0.09 |

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/senegal-whatsapp-disinformation-detector
cd senegal-whatsapp-disinformation-detector