# 🤖 AI Resume Screening System

[Live Demo](https://resume-ai-api-h8mx.onrender.com)


## Project Description
This project is an AI-powered resume screening system that allows users to upload their PDF resumes and receive instant analysis of their suitability for various job roles. The system extracts skills, preprocesses the text, predicts top job categories, and provides a suitability score.


## Features
- Upload PDF resumes and analyze them instantly
- Shows top-3 predicted job categories with probabilities
- Calculates a suitability score for each candidate
- Beautiful, interactive frontend with animated loader

  

## Model Architecture / Pipeline
<img width="611" height="231" alt="AI architecture drawio" src="https://github.com/user-attachments/assets/5e017e28-399d-401d-a35c-373745e04a5f" />



**Pipeline Steps:**
1. **PDF Upload** – Users upload their resume in PDF format  
2. **Text Extraction** – Extract text using `PyPDF2`  
3. **Preprocessing** – Convert text to lowercase, remove symbols  
4. **Vectorization** – Convert text into numerical features using TF-IDF  
5. **Model** – Logistic Regression predicts job category probabilities  
6. **Output** – Returns top-3 job roles + probability + suitability score  
7. **Frontend** – FastAPI serves the UI and API endpoints  



## Technologies Used
- Python 3  
- FastAPI  
- scikit-learn  
- Pandas / NumPy  
- PyPDF2  
- HTML, CSS, JavaScript  


## How to Run Locally
1. Clone the repository:
```bash
git clone https://github.com/adermgram/resume-ai-project.git
```
2. Install dependencies:
 ```
   pip install -r requirements.txt
```
3. Run the app:
 ```
   uvicorn app.api:app --reload
```

