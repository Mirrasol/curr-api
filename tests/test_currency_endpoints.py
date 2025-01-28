from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_show_currencies_route():
    user_data = {'username': 'Wyll', 'password': '_prideofthegate_'}
    response_login = client.post('/auth/login/', data=user_data)
    access_token = response_login.json()['access_token']

    authorized_headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/currency/list/', headers=authorized_headers)
    assert response.status_code == 200


def test_exchange_currency_route():
    user_data = {'username': 'Wyll', 'password': '_prideofthegate_'}
    response_login = client.post('/auth/login/', data=user_data)
    access_token = response_login.json()['access_token']

    authorized_headers = {'Authorization': f'Bearer {access_token}'}
    exchange_data = {"from_currency": "usd", "to_currency": "cad", "amount": 16}
    response = client.post(
        '/currency/exchange/',
        params=exchange_data,
        headers=authorized_headers,
        )
    assert response.status_code == 200
