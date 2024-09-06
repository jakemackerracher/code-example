import pytest
from models import User
from faker import Faker
from base import db

fake = Faker()

def test_auth_logout_endpoint_sucessful(client):
    email = fake.email()
    password = fake.password()

    # TODO: replace below with a database call to create user directly
    response = client.post('/auth/register', json={
        "name": fake.name(),
        "email": email,
        "password": password
    })
    assert response.status_code == 201

    response = client.post('/auth/login', json={
        "email": email,
        "password": password
    })
    assert response.status_code == 204

    response = client.get('/auth/logout')
    assert response.status_code == 204

def test_auth_logout_endpoint_not_logged_in(client):
    response = client.get('/auth/logout')
    assert response.status_code == 401