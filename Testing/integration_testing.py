import pytest
from app import app, users

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_integration_signup_and_login(client):
    # Signup
    response = client.post('/signup', data=dict(
        username='integrationuser', password='integrationpass'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Signup successful! Please log in.' in response.data

    # Login
    response = client.post('/login', data=dict(
        username='integrationuser', password='integrationpass'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Login successful!' in response.data
