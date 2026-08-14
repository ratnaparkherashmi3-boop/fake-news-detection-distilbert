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
  |
  v
HTML + CSS + JavaScript
  |
  v
JavaScript Fetch API
  |
  v
Flask REST API
  |
  v
DistilBERT NLP Model
  |
  v
Binary Classification
  |
  +-------------------+
  |                   |
  v                   v
Fake News       Factual News
  |
  v
Confidence Score
  |
  v
Frontend Result
