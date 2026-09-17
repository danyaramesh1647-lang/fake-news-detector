# Fake News Detector

### NLP-Based Fake News Detection using Machine Learning and Flask

🔗 **Live Demo:** https://fake-news-detector-g9ei.onrender.com

---

## 📌 Project Overview

Fake News Detector is an NLP-based web application that analyzes a given news statement and predicts whether it is **REAL** or **FAKE** using a trained Machine Learning classification model.

The application provides a simple interface where users can enter a news statement and receive a prediction along with a model confidence score.

## 🚀 Features

- 📰 Analyze news statements
- 🤖 Machine Learning-based classification
- 🧠 NLP-based text processing
- 📊 REAL / FAKE prediction
- 📈 Confidence score
- 🌐 Flask web application
- ☁️ Deployed online

## 🛠️ Technologies Used

- Python
- Flask
- Natural Language Processing (NLP)
- Scikit-learn
- TF-IDF Vectorization
- Passive Aggressive Classifier
- Pandas
- HTML
- CSS
- JavaScript

## ⚙️ How It Works

```text
User enters news statement
          ↓
Text preprocessing
          ↓
TF-IDF Vectorization
          ↓
Machine Learning Model
          ↓
REAL / FAKE Prediction
          ↓
Confidence Score

📂 Dataset

The project uses a synthetic dataset containing:

600 REAL examples
600 FAKE examples
1,200 total examples
📊 Model Performance

The model achieved 100% accuracy on the held-out test portion of the synthetic dataset.

Note: This result represents performance on the synthetic dataset and should not be interpreted as 100% real-world fake-news detection accuracy.

⚠️ Disclaimer

This application provides a statistical prediction from a trained text-classification model. It is not a fact-checking system.

Important claims should always be cross-checked with reliable and authoritative sources.

📁 Project Structure
fake-news-detector/
│
├── app.py
├── train_model.py
├── generate_dataset.py
├── dataset.csv
├── requirements.txt
├── Procfile
├── README.md
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
👩‍💻 Author

Danya R