import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

from preprocess import load_and_clean_data

# Load data
df = load_and_clean_data("data/resumes.csv")

X = df["resume_text"]
y = df["category"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/trained_model.pkl")

print("Model trained and saved successfully!")