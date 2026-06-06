from fastapi import FastAPI
from api.schemas import PredictRequest, PredictResponse
from api.predictor import Predictor

predictor = Predictor()

app = FastAPI(title="Symptom Classifier")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    result = predictor.predict(req.symptoms)
    return result