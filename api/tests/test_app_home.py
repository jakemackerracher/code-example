import pytest

def test_app_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Flask!' in response.data