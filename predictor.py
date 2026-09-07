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


def predict_sms(message):
    processed_message = preprocess_stem(message)
    vectorized_message = vectorizer.transform([processed_message])
    prediction = model.predict(vectorized_message)[0]

    if prediction == 1:
        return "spam"
    else:
        return "ham"