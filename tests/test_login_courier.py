import requests
import allure
import pytest
from helpers.urls import LOGIN_COURIER_URL


@allure.epic("Логин курьера")
class TestCourierLogin:

    @allure.title("Курьер может авторизоваться")
    def test_courier_can_login(self, create_and_delete_courier):
        response = requests.post(LOGIN_COURIER_URL, json={
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"]
        })

        assert response.status_code == 200, f"Ошибка при логине курьера: {response.text}"
        assert "id" in response.json(), "Отсутствует id в ответе"

    @allure.title("Авторизация требует логин")
    def test_login_missing_login_field(self):
        invalid_data = {
            "password": "test_password"  # Логин отсутствует
        }

        response = requests.post(LOGIN_COURIER_URL, json=invalid_data)

        assert response.status_code == 400, f"Ошибка: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка при вводе некорректного логина или пароля")
    @pytest.mark.parametrize("login, password", [
        ("wrong_login", "test_password"),  # Неверный логин
        ("test_login", "wrong_password") # Неверный пароль
    ])
    def test_login_incorrect_credentials(self, login, password):
        response = requests.post(LOGIN_COURIER_URL, json={"login": login, "password": password})
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка при логине несуществующего пользователя")
    def test_login_non_existent_user(self):
        response = requests.post(LOGIN_COURIER_URL, json={"login": "non_existent", "password": "wrong_pass"})
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
