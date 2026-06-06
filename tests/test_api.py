import pytest
from fastapi.testclient import TestClient


def test_health():
    """API health check returns ok."""
    from api.main import app
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_missing_field():
    """Missing symptoms field should return 422 validation error."""
    from api.main import app
    client = TestClient(app)
    response = client.post("/predict", json={})
    assert response.status_code == 422