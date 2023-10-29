import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Iris Flower Species Predictor" in response.data

def test_predict_endpoint(client):
    data = {
        'sepal_length': '5.1',
        'sepal_width': '3.5',
        'petal_length': '1.4',
        'petal_width': '0.2'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b"Prediction:" in response.data