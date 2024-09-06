import pytest
from faker import Faker

fake = Faker()

def test_auth_register_endpoint_sucessful(client):
    response = client.post('/auth/register', json={
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password()
    })
    assert response.status_code == 201

def test_auth_register_endpoint_user_already_registered(client):
    json={
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password()
    }
    response = client.post('/auth/register', json=json)
    assert response.status_code == 201

    response = client.post('/auth/register', json=json)
    assert response.status_code == 409
    assert response.is_json

    json_data = response.get_json()
    assert json_data == {'error': 'User already registered'}

def test_auth_register_endpoint_requires_name(client):
    response = client.post('/auth/register', json={
        "email": fake.email(),
        "password": fake.password()
    })
    assert response.status_code == 400
    assert response.is_json

    json_data = response.get_json()
    assert json_data == {'error': 'Missing required fields'}


def test_auth_register_endpoint_requires_email(client):
    response = client.post('/auth/register', json={
        "name": fake.name(),
        "password": fake.password()
    })
    assert response.status_code == 400
    assert response.is_json

    json_data = response.get_json()
    assert json_data == {'error': 'Missing required fields'}

def test_auth_register_endpoint_requires_password(client):
    response = client.post('/auth/register', json={
        "name": fake.name(),
        "email": fake.email()
    })
    assert response.status_code == 400
    assert response.is_json

    json_data = response.get_json()
    assert json_data == {'error': 'Missing required fields'}
