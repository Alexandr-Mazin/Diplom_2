import allure
import requests
from data import Url, OrderTest

class TestGetUserOrder:

    @allure.description('Получение заказа авторизованным пользователем')
    @allure.title('Получение заказа авторизованным пользователем')
    def test_get_user_order_with_auth_success(self, test_user):
        test_user_data, response_body, status_code = test_user

        access_token = response_body.get('accessToken')
        order = {'ingredients': OrderTest.list_ingredients['ingredients']}
        requests.post(Url.order_create, headers={"Authorization": access_token}, data=order)

        response = requests.get(Url.get_orders, headers={"Authorization": access_token})

        deserials = response.json()

        assert response.status_code == 200
        assert deserials['success'] is True
        assert len(response.json()["orders"]) == 1

    @allure.description('Получение заказа не авторизованным пользователем')
    @allure.title('Получение заказа не авторизованным пользователем')
    def test_get_user_order_without_auth_success(self):

        response = requests.get(Url.get_orders)

        deserials = response.json()

        assert response.status_code == 401
        assert deserials['message'] == "You should be authorised"
