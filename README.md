# AI-Powered Fake News Detection System

An end-to-end NLP-based Fake News Detection system using a fine-tuned DistilBERT transformer model to classify news articles as **Fake News** or **Factual News**.

## Project Overview

This project analyzes a news headline and article and predicts whether the content is Fake News or Factual News.

The system combines a trained NLP model with a Flask REST API and a web-based frontend.

## Features

- Fake News vs Factual News classification
- DistilBERT-based NLP model
- News headline and article input
- Real-time prediction
- Prediction confidence score
- Flask REST API
- HTML, CSS and JavaScript frontend

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

## Project Architecture

User
↓
HTML + CSS + JavaScript
↓
Flask REST API
↓
DistilBERT NLP Model
↓
Fake News / Factual News
↓
Confidence Score
↓
Frontend Result

## Classification

| Label | Class |
|------:|-------|
| 0 | Factual News |
| 1 | Fake News |

## How It Works

1. User enters a news headline and article.
2. JavaScript sends the input to the Flask API.
3. Flask receives the request.
4. The text is processed by the DistilBERT model.
5. The model predicts the news category.
6. The API returns the prediction and confidence score.
7. The result is displayed on the frontend.

## API

### Endpoint

POST /predict

### Request

{
  "title": "News headline",
  "text": "News article content"
}

### Response

{
  "prediction": "Fake News",
  "confidence": 50.34
}

## Project Files

- `Fake_News_DL.ipynb` — Model training and experimentation
- `fake_news_dl.py` — Python backend/model code
- `index.html` — Frontend structure
- `style.css` — Frontend styling
- `script.js` — Frontend/API integration

## Future Improvements

- Improve model performance
- Add precision, recall and F1-score
- Add confusion matrix
- Improve handling of long articles
- Add prediction history
- Deploy the application on a permanent cloud platform

## Author

**Rashmi Ratnaparkhe**

AI/ML | Python | NLP | Machine Learning