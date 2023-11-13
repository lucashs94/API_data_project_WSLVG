from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()


produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um otimo telefone",
        "preco": 1500,
        "disponivel": True,
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um otimo Notebook",
        "preco": 3500,
        "disponivel": False,
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Um otimo Tablet",
        "preco": 2500,
        "disponivel": True,
    },
]


@app.get('/')
def hello():
    return { 'Ola':'Mundo' }


@app.get('/produtos')
def listar_produtos():
    return produtos


@app.get('/produtos/{id}')
def buscar_produto(id: int):
    for produto in produtos:
        if produto['id'] == id:
            return produto
    
    return { 'Status': 404, 'Message':'Product not found' }
            