import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session_id(client):
    return client.post("/sessions").json()["session_id"]
