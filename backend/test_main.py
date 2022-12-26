from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_all_blogs():
    response = client.get('/blogs/')
    assert response.status_code == 200


def test_auth_errors():
    response = client.post(
        '/token/',
        data={
            'username': '',
            'password': ''
        }
    )
    access_token = response.json().get('access_token')

    assert access_token is None

    message = response.json().get('detail')[0].get('msg')

    assert message == 'field required'


def test_auth_correct():
    response = client.post(
        '/token/',
        data={
            'username': 'altyofficial',
            'password': 'solo3224'
        }
    )

    access_token = response.json().get('access_token')

    assert access_token is not None


def test_article_with_auth():
    auth = client.post(
        '/token/',
        data={
            'username': 'altyofficial',
            'password': 'solo3224'
        }
    )

    access_token = auth.json().get('access_token')

    response = client.get('/articles/1/')

    assert response.status_code == 401
    
    response = client.get(
        '/articles/1/',
        headers={
            'Authorization': f'Bearer {access_token}'
        }
    )

    assert response.status_code == 200
