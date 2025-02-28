import requests
import allure
from data import Url, OrderTest


class TestCreateOrder:

    @allure.description('Создание заказа авторизованным пользователем')
    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_with_auth_success(self, test_user):
        test_user_data, response_body, status_code = test_user
        access_token = response_body.get('accessToken')

        order = {'ingredients': OrderTest.list_ingredients['ingredients']}
        response = requests.post(Url.order_create, headers={"Authorization": access_token}, data=order)
        deserials = response.json()

        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'number' in deserials.get('order', {})

    @allure.description('Создание заказа без авторизации')
    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth_success(self):
        order = {'ingredients': OrderTest.list_ingredients['ingredients']}
        response = requests.post(Url.order_create, data=order)
        deserials = response.json()

        assert response.status_code == 200, "Ожидался код ответа 200."
        assert deserials.get('success') is True
        assert 'number' in deserials.get('order', {})

    @allure.description('Создание заказа c ингредиентами')
    @allure.title('Создание заказа c ингредиентами')
    def test_create_order_with_auth_success_ingredients(self, test_user):
        test_user_data, response_body, status_code = test_user
        access_token = response_body.get('accessToken')

        order = {'ingredients': OrderTest.list_ingredients['ingredients']}
        response = requests.post(Url.order_create, headers={"Authorization": access_token}, data=order)
        deserials = response.json()

        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'number' in deserials.get('order', {})


    @allure.description('Создание заказа без ингредиентов')
    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, test_user):
        test_user_data, response_body, status_code = test_user
        access_token = response_body.get('accessToken')

        response = requests.post(Url.order_create, headers={"Authorization": access_token})
        deserials = response.json()

        assert response.status_code == 400
        assert deserials['success'] is False
        assert deserials['message'] == "Ingredient ids must be provided"

    @allure.description('Создание заказа с неверным хешем ингредиентов')
    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredient_hash(self, test_user):
        test_user_data, response_body, status_code = test_user
        access_token = response_body.get('accessToken')

        order = {'ingredients': OrderTest.wrong_list_ingredients['ingredients']}
        response = requests.post(Url.order_create, headers={"Authorization": access_token}, data=order)

        assert response.status_code == 500