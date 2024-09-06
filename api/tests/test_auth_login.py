import pytest
from models import User
from faker import Faker
from base import db

fake = Faker()

def test_auth_login_endpoint_sucessful(client):
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

def test_auth_login_endpoint_invalid_email(client):
    response = client.post('/auth/login', json={
        "email": fake.email(),
        "password": fake.password()
    })
    assert response.status_code == 404
    assert response.is_json

    json_data = response.get_json()
    assert json_data == {'error': 'Invalid credentials'}

def test_auth_login_endpoint_invalid_password(client):
    email = fake.email()
    password = fake.password()
    another_password = fake.password()

    # TODO: replace below with a database call to create user directly
    response = client.post('/auth/register', json={
        "name": fake.name(),
        "email": email,
        "password": password
    })
    assert response.status_code == 201

    response = client.post('/auth/login', json={
        "email": email,
        "password": another_password
    })
    assert response.status_code == 404
    assert response.is_json

    json_data = response.get_json()
    assert json_data == {'error': 'Invalid credentials'}

def test_auth_login_endpoint_requires_email(client):
    response = client.post('/auth/login', json={
        "password": fake.password()
    })
    assert response.status_code == 400
    assert response.is_json

    json_data = response.get_json()
    assert json_data == {'error': 'Missing required fields'}

def test_auth_login_endpoint_requires_password(client):
    response = client.post('/auth/login', json={
        "email": fake.email()
    })
    assert response.status_code == 400
    assert response.is_json

    json_data = response.get_json()
    assert json_data == {'error': 'Missing required fields'}
