import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from joblib import load
import numpy as np
import os

# Paths
MODEL_PATH = os.path.join("models", "model.joblib")
VECTORIZER_PATH = os.path.join("models", "vectorizer.joblib")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load model & vectorizer
model = None
vectorizer = None

@app.on_event("startup")
def load_artifacts():
    global model, vectorizer
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError(f"Place your model at {MODEL_PATH} and vectorizer at {VECTORIZER_PATH}")
    model = load(MODEL_PATH)
    vectorizer = load(VECTORIZER_PATH)
    print("✅ Model and vectorizer loaded.")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict_api(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if not text:
        return JSONResponse({"error": "No text provided"}, status_code=400)

    X = vectorizer.transform([text])

    # Predict probability
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)[0][1]
    else:
        try:
            scores = model.decision_function(X)
            proba = 1 / (1 + np.exp(-scores[0]))
        except Exception:
            pred = model.predict(X)[0]
            proba = float(pred)

    proba = max(0.0, min(1.0, proba))
    label = "Spam" if proba >= 0.5 else "Not Spam"

    return JSONResponse({
        "prediction": label.lower(),
        "probability": proba
    })

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
