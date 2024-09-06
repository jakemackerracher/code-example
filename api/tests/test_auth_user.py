import pytest
from models import User
from faker import Faker

fake = Faker()

def test_auth_user_endpoint_sucessful(client):
    name = fake.name()
    email = fake.email()
    password = fake.password()

    # TODO: replace below with a database call to create user directly
    response = client.post('/auth/register', json={
        "name": name,
        "email": email,
        "password": password
    })
    assert response.status_code == 201

    user = User.query.filter_by(email=email).first()
    assert user

    response = client.post('/auth/login', json={
        "email": email,
        "password": password
    })
    assert response.status_code == 204

    response = client.get('/auth/user')
    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()
    assert data.get('id') == user.id
    assert data.get('name') == name
    assert data.get('email') == email
    assert data.get('password') == None
    assert data.get('is_admin') == user.is_admin

def test_auth_user_endpoint_no_user(client):
    response = client.get('/auth/user')
    assert response.status_code == 401
