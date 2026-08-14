# AI-Powered Fake News Detection System

An end-to-end NLP-based Fake News Detection system using a fine-tuned DistilBERT transformer model to classify news articles as **Fake News** or **Factual News**.

## Project Overview

This project analyzes a news headline and article and predicts whether the content is Fake News or Factual News.

The system combines a trained NLP model with a Flask REST API and a web-based frontend for real-time predictions.

## Features

- Fake News vs Factual News classification
- DistilBERT-based NLP model
- News headline and article input
- Real-time prediction
- Prediction confidence score
- Flask REST API
- HTML, CSS and JavaScript frontend
- Frontend-to-backend API integration

## Technologies Used

- Python
- NLP
- Machine Learning
- Deep Learning
- DistilBERT
- Hugging Face Transformers
- PyTorch
- Flask
- Flask-CORS
- HTML5
- CSS3
- JavaScript
- Google Colab
- GitHub

## Project Architecture

User
  ↓
HTML + CSS + JavaScript
  ↓
JavaScript Fetch API
  ↓
Flask REST API
  ↓
DistilBERT NLP Model
  ↓
Binary Classification
  ↓
Fake News / Factual News
  ↓
Confidence Score
  ↓
Frontend Result

Model Limitations

This project is an AI-assisted text classification system and should not be considered a definitive fact-checking system.

The prediction depends on patterns learned from the training dataset. A high confidence score does not guarantee that a news article is factually true or false.

The system should therefore be used as a classification tool and not as a replacement for professional fact-checking.

Future Improvements
Improve model performance through hyperparameter tuning
Add precision, recall and F1-score reporting
Add confusion matrix visualization
Improve handling of long articles
Add prediction history
Improve frontend user experience
Deploy the backend on a permanent cloud platform
Add model explainability
Add automated model monitoring
Author

Rashmi Ratnaparkhe

AI/ML | Python | NLP | Machine Learning
