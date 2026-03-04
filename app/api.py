from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
from PyPDF2 import PdfReader

model = joblib.load("models/trained_model.pkl")

app = FastAPI(title="AI Resume Screening API")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


def extract_text_from_pdf(file: UploadFile):
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


@app.post("/predict_pdf")
def predict_resume_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)

    probabilities = model.predict_proba([text])[0]
    categories = model.classes_

    results = list(zip(categories, probabilities))
    results_sorted = sorted(results, key=lambda x: x[1], reverse=True)
    top_3 = results_sorted[:3]

    top_category, top_probability = top_3[0]
    suitability_score = round(top_probability * 100, 2)

    top_3_formatted = [
        {"category": cat, "probability": round(float(prob), 3)}
        for cat, prob in top_3
    ]

    return {
        "file_name": file.filename,
        "top_prediction": top_category,
        "suitability_score": suitability_score,
        "top_3_matches": top_3_formatted
    }



# ---------------- TEXT PREDICTION ----------------
# @app.post("/predict")
# def predict_resume(data: ResumeRequest):
#     text = data.resume_text

#     probabilities = model.predict_proba([text])[0]
#     categories = model.classes_

#     results = list(zip(categories, probabilities))
#     results_sorted = sorted(results, key=lambda x: x[1], reverse=True)

#     top_3 = results_sorted[:3]

#     top_category, top_probability = top_3[0]
#     suitability_score = round(top_probability * 100, 2)

#     top_3_formatted = [
#         {"category": cat, "probability": round(float(prob), 3)}
#         for cat, prob in top_3
#     ]

#     return {
#         "top_prediction": top_category,
#         "suitability_score": suitability_score,
#         "top_3_matches": top_3_formatted
#     }