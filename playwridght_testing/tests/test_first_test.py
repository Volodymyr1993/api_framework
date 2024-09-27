# tests/test_endpoints.py
def test_get_posts(base_url, session):
    response = session.get(f"{base_url}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_post(base_url, session):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = session.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"
