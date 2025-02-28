import allure
import requests
from data import Url


class TestCreateUser:
    @allure.description('Проверка создания пользователя')
    @allure.title('Проверка создания пользователя')
    def test_create_user(self, test_user):
        payload, response_body, status_code = test_user
        assert status_code == 200, "Ожидался код ответа 200."
        assert response_body['success'] is True, "Ожидался успешный ответ."
        assert 'accessToken' in response_body, "Токен доступа отсутствует в ответе."
        assert 'refreshToken' in response_body, "Refresh-токен отсутствует в ответе."
        assert response_body['user']['email'] == payload['email'], "Email не совпадает."
        assert response_body['user']['name'] == payload['name'], "Имя не совпадает."


    @allure.description('Проверка создания пользователя, который уже зарегистрирован')
    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self, test_user):
        test_user_data, response_body, status_code = test_user

        response = requests.post(Url.user_register, json=test_user_data)
        deserials = response.json()

        assert response.status_code == 403
        assert deserials['success'] is False
        assert deserials['message'] == "User already exists"


    @allure.description('Проверка создания пользователя, без обязательного параметра')
    @allure.title('Создания пользователя, без обязательного параметра')
    def test_create_user_without_required_fields(self):
        test_user_data_list = [
            {"email": "", "password": "password", "name": "Test User"},
            {"email": "test@example.com", "password": "", "name": "Test User"},
            {"email": "test@example.com", "password": "password", "name": ""}
        ]

        for test_user_data in test_user_data_list:
            response = requests.post(Url.user_register, json=test_user_data)
            deserials = response.json()

            assert response.status_code == 403
            assert deserials['success'] is False
            assert deserials['message'] == "Email, password and name are required fields"