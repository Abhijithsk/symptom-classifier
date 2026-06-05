from pydantic import BaseModel

class PredictRequest(BaseModel):
    symptoms: str

class PredictResponse(BaseModel):
    disease: str
    confidence: float