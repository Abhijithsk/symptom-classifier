from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}

def test_predict_missing_field():
    response = client.post('/predict', json={})
    assert response.status_code == 422
