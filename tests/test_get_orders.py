import requests
import allure
from helpers.urls import GET_ORDERS_URL

@allure.epic("Список заказов")
class TestGetOrders:

    @allure.title("Список заказов возвращается корректно")
    def test_get_orders_list(self):
        response = requests.get(GET_ORDERS_URL)

        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert "orders" in response.json(), "Ответ не содержит ключ 'orders'"
        assert isinstance(response.json()["orders"], list), "'orders' не является списком"
