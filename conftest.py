import pytest
import requests
from helpers.urls import CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL
from helpers.data import get_valid_courier


@pytest.fixture
def create_and_delete_courier():
    courier = get_valid_courier()

    # Создание курьера
    create_response = requests.post(CREATE_COURIER_URL, json=courier)

    # Логинимся, чтобы получить ID курьера
    login_response = requests.post(LOGIN_COURIER_URL, json={
        "login": courier["login"],
        "password": courier["password"]
    })

    courier_id = login_response.json().get("id")

    yield courier

    # Удаление курьера
    delete_response = requests.delete(DELETE_COURIER_URL.format(courier_id=courier_id))
