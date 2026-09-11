from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_session_recommendation_feedback_and_delete():
    session_id = client.post("/sessions").json()["session_id"]
    response = client.post("/recommend", json={"session_id": session_id, "prompt": "warm beach trip for food and culture around $2000"})
    assert response.status_code == 200
    assert len(response.json()["recommendations"]) == 3
    assert client.post("/feedback", json={"session_id": session_id, "rating": 5}).status_code == 200
    assert client.delete(f"/sessions/{session_id}").status_code == 204
    assert client.post("/recommend", json={"session_id": session_id, "prompt": "a trip with food and culture"}).status_code == 404
