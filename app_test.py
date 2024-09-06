import pytest
from app import app

@pytest.fixture
def client():
  app.config['TESTING'] = True
  with app.test_client() as client:
    yield client

def test_home(client):
  rv = client.get('/')
  assert rv.data == b'Welcome to CI/CD Pipeline using Python!'
