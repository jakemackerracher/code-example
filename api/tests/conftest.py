import pytest
from app import app

@pytest.fixture(autouse=True)
def client():
    with app.test_client() as client:
        yield client