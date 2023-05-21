import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'todos' in data
    assert isinstance(data['todos'], list)

def test_add_todo(client):
    response = client.post('/add', json={'todo': 'Test Todo'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'todo' in data
    assert data['todo'] == 'Test Todo'

def test_delete_todo(client):
    # Add a todo first
    client.post('/add', json={'todo': 'Test Todo'})

    response = client.post('/delete', json={'todo': 'Test Todo'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'status' in data
    assert data['status'] == 'success'
