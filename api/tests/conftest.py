import pytest
from app import app

# TODO: Run tests within a separate database soley for testing

@pytest.fixture(autouse=True)
def client():
    with app.test_client() as client:
        yield client