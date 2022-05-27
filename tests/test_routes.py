import json

from fastapi.testclient import TestClient

from app.chatlet.models.auth import AccessToken
from core.main import app

client = TestClient(app)


def test_login():
    request = {
        "email": "user@example.com",
        "password": "string"
    }
    # expected_response = {
    #     "access_token": AccessToken.access_token,
    #     'access_token_expires': AccessToken.access_token_expires
    # }

    response = client.post('/auth/login', data=json.dumps(request), )

    assert response.status_code == 200
    # assert response.json() == expected_response


def test_registration():
    request = {
        "email": "user@exaample.com",
        "password": "string"
    }

    expected_response = {
        "email": "user@example.com"
    }

    response = client.post('/register', data=json.dumps(request), )

    assert response.status_code == 200
    assert response.json() == expected_response


def test_forgot_password():
    request = {
        "email": "user@example.com"
    }

    response = client.post('/password/forgot', data=json.dumps(request), )

    assert response.status_code == 200


def test_get_user():
    response = client.get('/user')

    assert response.status_code == 401


def test_delete_user():
    response = client.get('/user')
    assert response.status_code == 401


def test_update_user():
    request = {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com"
    }

    response = client.patch('/user', data=json.dumps(request), )

    assert response.status_code == 401


def test_get_chat():
    expected_response = [
        {
            "theme": "string",
            "room_name": "string",
            "members": [],
            "created_at": "2021-11-26T15:40:17.961000"
        },
        {
            "theme": "string",
            "room_name": "string",
            "members": [],
            "created_at": "2021-11-27T08:29:50.407000"
        }
    ]
    response = client.get('/chat/get')

    assert response.status_code == 200
    assert response.json() == expected_response


def test_create_chat():
    request = {
        "theme": "string",
        "room_name": "string",
        "members": [],
        "created_at": "2021-11-28T13:47:52.704850",
        "messages": []
    }

    response = client.post('/chat/create-chat', data=json.dumps(request), )

    assert response.status_code == 401
