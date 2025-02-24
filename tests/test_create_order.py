import requests
import allure
import pytest
from helpers.urls import CREATE_ORDER_URL
from helpers.data import get_order_data


@allure.epic("Создание заказа")
class TestCreateOrder:

    @allure.title("Можно создать заказ с разными вариантами цвета")
    @pytest.mark.parametrize("color", [
        ["BLACK"],  # Только черный
        ["GREY"],  # Только серый
        ["BLACK", "GREY"],  # Оба цвета
        []  # Без цвета
    ])
    def test_create_order_with_various_colors(self, color):
        order_data = get_order_data(color)

        response = requests.post(CREATE_ORDER_URL, json=order_data)

        assert response.status_code == 201, f"Ошибка при создании заказа: {response.text}"
        assert "track" in response.json(), "Ответ не содержит track"
