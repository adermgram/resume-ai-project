import joblib

model = joblib.load("models/trained_model.pkl")

def predict_resume(text):
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text]).max()
    return prediction, probability

if __name__ == "__main__":
    text = "Experienced SEO specialist and digital marketing professional"
    pred, prob = predict_resume(text)
    print(pred, prob)