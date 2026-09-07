import streamlit as st
from predictor import predict_sms

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
        prediction = predict_sms(message)

        if prediction == "spam":
            st.error("🚨 This message is SPAM")
        else:
            st.success("✅ This message is HAM")