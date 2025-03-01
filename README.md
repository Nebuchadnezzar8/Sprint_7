# Sprint_7

## Описание проекта
Автотесты API для сервиса заказа самокатов

## Структура проекта
- **helpers/**: Содержит вспомогательные модули.
  - `data.py`: Тестовые данные.
  - `urls.py`: Хранение URL-адресов, используемых в тестах.
- **tests/**: Содержит тесты.
  - `test_create_courier`: Тесты для создания курьеров.
  - `test_login_courier`: Тесты для авторизации курьеров.
  - `test_create_order`: Тесты для создания заказа.
  - `test_get_orders`: Тесты для получения заказа.
- **конфигурационные файлы**:
  - `.gitignore`: Исключение файлов из контроля версий.
  - `conftest.py`: Фикстуры и общие настройки для тестов.
  - `pytest.ini`: Настройки для Pytest.
  - `requirements.txt`: Список зависимостей.

## Требования
- Python 3.x
- Pytest  
- Allure  

## Установка
1. Клонируйте репозиторий:  
   ```bash
   git clone https://github.com/Nebuchadnezzar8/Sprint_7.git

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt

## Запуск тестов:
    pytest


## Сформировать отчет в Allure:
   ```bash
   allure serve allure_results
