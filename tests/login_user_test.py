import pytest
import allure
import requests
from data import Url


class TestLoginUser:

    @allure.description('Проверка логина под существующим пользователем')
    @allure.title('Успешная авторизация под существующим пользователем')
    def test_login_existing_user(self, test_user):
        test_user_data, response_body, status_code = test_user

        payload = {
            "email": test_user_data['email'],
            "password": test_user_data['password']
        }

        response = requests.post(Url.user_login, json=payload)
        deserials = response.json()

        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'accessToken' in deserials.keys()
        assert 'refreshToken' in deserials.keys()
        assert deserials['user']['email'] == test_user_data['email']
        assert deserials['user']['name'] == test_user_data['name']

    @allure.description('Проверка логина с неверными данными')
    @allure.title('Логин с неверным логином и паролем')
    @pytest.mark.parametrize("test_input", [
        {"email": "wrong@example.com", "password": "wrongpassword"},
        {"email": "test@example.com", "password": "wrongpassword"},
        {"email": "wrong@example.com", "password": "password"},
        {"email": "", "password": "password"},
        {"email": "test@example.com", "password": ""},
        {"email": "", "password": ""}
    ])
    def test_login_invalid_user(self, test_input):
        response = requests.post(Url.user_login, json=test_input)
        deserials = response.json()

        assert response.status_code == 401
        assert deserials['success'] is False
        assert deserials['message'] == "email or password are incorrect"