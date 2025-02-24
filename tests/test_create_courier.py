import requests
import allure
import pytest
from helpers.urls import CREATE_COURIER_URL
from helpers.data import get_valid_courier


@allure.epic("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self):
        courier_data = get_valid_courier()
        response = requests.post(CREATE_COURIER_URL, json=courier_data)

        assert response.status_code == 201, f"Ошибка: {response.text}"
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, create_and_delete_courier):
        response = requests.post(CREATE_COURIER_URL, json=create_and_delete_courier)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера требует обязательных полей (login, password)")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field(self, missing_field):
        courier_data = get_valid_courier()
        del courier_data[missing_field]
        response = requests.post(CREATE_COURIER_URL, json=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Запрос возвращает правильный код ответа")
    def test_create_courier_status_code(self):
        courier_data = get_valid_courier()
        response = requests.post(CREATE_COURIER_URL, json=courier_data)
        assert response.status_code == 201
