import streamlit as st
import pickle
import re
from nltk.stem import PorterStemmer

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

stemmer = PorterStemmer()

def preprocess_stem(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    return " ".join(stemmed_words)


st.set_page_config(
    page_title="SMS Spam Classifier",
    page_icon="📱",
    layout="centered"
)

st.title("📱 SMS Spam Classifier")
st.write("Enter an SMS message below to check whether it is spam or ham.")

message = st.text_area(
    "Enter your message:",
    placeholder="Example: Congratulations! You have won a free prize!"
)

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter an SMS message.")
    else:
        processed_message = preprocess_stem(message)

        vectorized_message = vectorizer.transform([processed_message])

        prediction = model.predict(vectorized_message)[0]

        if prediction == 1:
            st.error("🚨 This message is SPAM")
        else:
            st.success("✅ This message is HAM")