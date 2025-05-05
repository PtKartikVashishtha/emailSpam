# app.py
import streamlit as st
import joblib
import string

model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def clean_input(text):
    return ''.join([ch for ch in text.lower() if ch not in string.punctuation])

st.title("📱 SMS Spam Classifier")
msg = st.text_area("Enter your SMS message:")

if st.button("Predict"):
    msg_clean = clean_input(msg)
    msg_vec = vectorizer.transform([msg_clean])
    prediction = model.predict(msg_vec)[0]

    if prediction == 1:
        st.error("🚫 Spam Message")
    else:
        st.success("✅ Not Spam (Ham)")
