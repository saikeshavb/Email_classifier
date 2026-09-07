from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predictor import predict_sms

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "chrome-extension://fnljnmilcnngbfjnklfdffniibghekda"
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


class SMSRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "SMS Spam Classifier API is running"}


@app.post("/predict")
def predict(request: SMSRequest):
    prediction = predict_sms(request.message)

    return {
        "prediction": prediction
    }