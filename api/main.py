from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.schemas import PredictRequest, PredictResponse
from api.predictor import Predictor

predictor = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global predictor
    predictor = Predictor()
    yield

app = FastAPI(title="Symptom Classifier", lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    result = predictor.predict(req.symptoms)
    return result