# SMS Spam Classifier

A Streamlit web app that classifies SMS messages as **spam** or **ham** using a trained machine-learning model.

## Project Files

- `app.py` - Streamlit application and message preprocessing logic.
- `model.pkl` - Trained classification model.
- `vectorizer.pkl` - Fitted text vectorizer used by the model.
- `SMS_Classifier.ipynb` - Notebook used for exploration and model training.

## Requirements

- Python 3.9 or later
- Streamlit
- scikit-learn
- NLTK

Install the Python dependencies with:

```bash
python -m pip install streamlit scikit-learn nltk
```

## Run the App

From the project directory, run:

```bash
streamlit run app.py
```

Streamlit will open the app in your browser. Enter an SMS message and select **Predict** to classify it.

## How It Works

1. The message is converted to lowercase.
2. Punctuation is removed.
3. Words are stemmed with NLTK's `PorterStemmer`.
4. The processed message is transformed with `vectorizer.pkl`.
5. The trained model from `model.pkl` predicts spam (`1`) or ham (`0`).

## Troubleshooting

- Run the command from the project directory so `model.pkl` and `vectorizer.pkl` can be found.
- If loading a model fails after changing scikit-learn versions, reinstall the version used when the model was trained.
- Only load the included pickle files or other trusted files. Pickle files can execute code when loaded.

## Retraining

Use `SMS_Classifier.ipynb` to inspect the training workflow or retrain the model. After retraining, replace both `model.pkl` and `vectorizer.pkl` together so they remain compatible.