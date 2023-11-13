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


def test_listar_produtos_status_code_200():
    response = client.get('/produtos')
    assert response.status_code == 200


def test_listar_produtos_tamanho_lista():
    response = client.get('/produtos')
    assert len(response.json()) == 3


def test_buscar_produto():
    response = client.get('/produtos/1')
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um otimo telefone",
        "preco": 1500,
        "disponivel": True,
    }    