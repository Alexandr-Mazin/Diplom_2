import pytest
import requests
from faker import Faker
from data import Url

fake = Faker()

@pytest.fixture(scope="function")
def test_user():
    test_user_data = {
        "email": fake.email(),
        "password": "password",
        "name": fake.name()
    }

    response = requests.post(Url.user_register, json=test_user_data)
    response_body = response.json()

    yield test_user_data, response_body, response.status_code

    access_token = response_body['accessToken']
    requests.delete(Url.user_delete, headers={'Authorization': access_token})