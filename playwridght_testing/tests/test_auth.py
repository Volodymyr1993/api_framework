# tests/test_auth.py

def test_authentication(base_url, session):
    # Replace with your actual authentication test
    response = session.post(f"{base_url}/auth", json={"username": "user", "password": "pass"})
    assert response.status_code == 200
    assert "token" in response.json()
