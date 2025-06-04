from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    r = client.post("/register", json={"email": "test@x.com", "password": "pass123"})
    assert r.status_code == 200

    token_res = client.post("/token", data={"username": "test@x.com", "password": "pass123"})
    assert "access_token" in token_res.json()
