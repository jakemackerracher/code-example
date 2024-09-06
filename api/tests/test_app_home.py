import pytest
from app import app

def test_app_home_endpoint():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello, Flask!' in response.data