import random
import string


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def get_valid_courier():
    return {
        "login": generate_random_string(),
        "password": "test_password",
        "firstName": "Test"
    }


def get_invalid_courier():
    return {
        "login": generate_random_string()
    }


def get_order_data(color=None):
    return {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": color or []
    }
