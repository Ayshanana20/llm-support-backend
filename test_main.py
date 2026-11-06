from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_support_endpoint_success():
    response = client.post(
        "/support",
        json={"question": "How do I update my profile?", "user_id": "test_user_99"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["model_used"] == "mock-gpt-4o-mini"
    assert "tokens_used" in data
    assert "cost_estimate_usd" in data

def test_support_endpoint_validation_error():
    # Sending invalid data (missing question, too short)
    response = client.post(
        "/support",
        json={"question": "Hi", "user_id": "test_user_99"}
    )
    assert response.status_code == 422