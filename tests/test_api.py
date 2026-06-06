import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_health():
    """API health check returns ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_returns_disease():
    """Predict endpoint returns disease and confidence for valid symptoms."""
    response = client.post("/predict", json={"symptoms": "fever headache chills"})
    assert response.status_code == 200
    data = response.json()
    assert "disease" in data
    assert "confidence" in data
    assert isinstance(data["disease"], str)
    assert len(data["disease"]) > 0


def test_predict_confidence_range():
    """Confidence score must be a valid probability between 0 and 1."""
    response = client.post("/predict", json={"symptoms": "fever headache chills"})
    assert response.status_code == 200
    confidence = response.json()["confidence"]
    assert 0.0 <= confidence <= 1.0


def test_predict_empty_symptoms():
    """Empty symptoms string should still return a valid response."""
    response = client.post("/predict", json={"symptoms": ""})
    assert response.status_code == 200
    assert "disease" in response.json()


def test_predict_unknown_symptoms():
    """Unknown symptom words should not crash the model."""
    response = client.post("/predict", json={"symptoms": "xyzabc unknownword"})
    assert response.status_code == 200
    assert "disease" in response.json()


def test_predict_missing_field():
    """Missing symptoms field should return 422 validation error."""
    response = client.post("/predict", json={})
    assert response.status_code == 422


def test_predict_multiple_symptoms():
    """Multiple symptoms should produce a confident prediction."""
    response = client.post(
        "/predict",
        json={"symptoms": "itching skin rash nodal skin eruptions dischromic patches"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["confidence"] > 0.5
