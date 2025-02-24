class Url:
    base_url = 'https://stellarburgers.nomoreparties.site'
    user_register = f'{base_url}/api/auth/register'
    user_login = f'{base_url}/api/auth/login'
    user_update = f'{base_url}/api/auth/user'
    user_delete = f'{base_url}/api/auth/user'
    order_create = f'{base_url}/api/orders'
    get_orders = f'{base_url}/api/orders'


class OrderTest:
    list_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]
    }

    wrong_list_ingredients = {
        "ingredients": ["123", "123", "123"]
    }

