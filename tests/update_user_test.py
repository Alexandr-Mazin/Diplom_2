import pytest
import allure
import requests
from data import Url

class TestUserData:

    @allure.description('Проверка обновления данных пользователя с авторизацией')
    @allure.title('Успешное обновление данных пользователя')
    @pytest.mark.parametrize("new_email, new_name", [
        (None, "Another Name"),
        ("another_email@test.ru", None),
    ])
    def test_update_user_email_and_name(self, test_user, new_email, new_name):
        test_user_data, response_body, status_code = test_user
        access_token = response_body['accessToken']

        update_data = {}
        if new_email is not None:
            update_data["email"] = new_email
        if new_name is not None:
            update_data["name"] = new_name

        headers = {"Authorization": access_token}
        response = requests.patch(Url.user_update, headers=headers, json=update_data)

        assert response.status_code == 200, "Ожидался код ответа 200."
        assert response.json().get('success') is True, "Ожидался успешный ответ."

    @allure.description('Проверка обновления данных пользователя без авторизации')
    @allure.title('Неуспешное обновление данных пользователя без авторизации')
    @pytest.mark.parametrize("new_email, new_name", [
        (None, "Another Name"),
        ("another_email@test.ru", None),
    ])
    def test_update_user_data_without_auth(self, test_user, new_email, new_name):

        update_data = {}
        if new_email is not None:
            update_data["email"] = new_email
        if new_name is not None:
            update_data["name"] = new_name

        response = requests.patch(Url.user_update, json=update_data)

        assert response.status_code == 401
        deserials = response.json()
        assert deserials['success'] is False
        assert deserials['message'] == "You should be authorised"