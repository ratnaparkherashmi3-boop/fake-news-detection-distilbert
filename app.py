import streamlit as st
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# Load cached model and tokenizer to optimize performance
@st.cache_resource
def load_model():
    tokenizer = DistilBertTokenizerFast.from_pretrained("./fake_news_model")[cite: 1]
    model = DistilBertForSequenceClassification.from_pretrained("./fake_news_model")[cite: 1]
    model.eval()[cite: 1]
    return tokenizer, model

tokenizer, model = load_model()

# User Interface
st.title("📰 Fake News Classifier")
st.write("Enter news headline and body text to verify credibility.")

title = st.text_input("Article Title")
text = st.text_area("Article Content", height=150)

if st.button("Predict"):
    if not title.strip() and not text.strip():
        st.warning("Please input a title or content to analyze.")
    else:
        input_text = f"{title} {text}".strip()[cite: 1]
        
        inputs = tokenizer(
            input_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )[cite: 1]

        with torch.no_grad():
            outputs = model(**inputs)[cite: 1]

        probabilities = torch.softmax(outputs.logits, dim=1)[cite: 1]
        predicted_class = torch.argmax(probabilities, dim=1).item()[cite: 1]
        confidence = probabilities[0][predicted_class].item() * 100[cite: 1]

        # 0 = Factual News, 1 = Fake News[cite: 1]
        if predicted_class == 0:
            st.success(f"**Prediction:** Factual News ({confidence:.2f}% confidence)")[cite: 1]
        else:
            st.error(f"**Prediction:** Fake News ({confidence:.2f}% confidence)")[cite: 1]
