import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_hello_status_code_200():
    response = client.get('/')
    assert response.status_code == 200


def test_hello_return_json():
    response = client.get('/')
    assert response.json() == { "Ola": "Mundo" }