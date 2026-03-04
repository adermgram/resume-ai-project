import pandas as pd
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df["resume_text"] = df["resume_text"].apply(clean_text)
    return df