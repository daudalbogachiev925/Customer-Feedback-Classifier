import streamlit as st
import pandas as pd
from classifier import classify

st.title("💬 Customer Feedback Classifier")

text = st.text_area("Отзыв клиента:", "App crashes when I try to upload a photo")
if st.button("Классифицировать"):
    st.json(classify(text))

st.subheader("Batch processing")
uploaded = st.file_uploader("CSV с колонкой 'text'", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    df["category"] = df["text"].apply(lambda x: classify(x)["category"])
    df["sentiment"] = df["text"].apply(lambda x: classify(x)["sentiment"])
    st.dataframe(df)
    st.download_button("Скачать", df.to_csv(index=False), "classified.csv")
