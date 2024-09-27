# tests/conftest.py
import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope="session")
def auth_token(base_url, session):
    # Replace with your API's authentication logic if needed
    # response = session.post(f"{base_url}/auth", json={"username": "user", "password": "pass"})
    # return response.json().get("token")
    # Placeholder for example
    return "dummy_token"

@pytest.fixture
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}
