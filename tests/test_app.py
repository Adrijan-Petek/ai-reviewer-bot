# tests/test_app.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_review_endpoint():
    payload = {"diff": "def foo():\n    return 42"}
    response = client.post("/review", json=payload)
    assert response.status_code == 200
    assert "summary" in response.json()
