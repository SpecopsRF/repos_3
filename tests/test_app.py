"""
Тесты для FastAPI приложения.
Используем httpx для асинхронного тестирования.
"""
import sys
import os

# Добавляем путь к приложению
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from fastapi.testclient import TestClient
from main import app

# Создаём тестовый клиент
client = TestClient(app)


def test_home_page():
    """Тест: главная страница возвращает код 200."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    print("✅ Главная страница работает!")


def test_health_endpoint():
    """Тест: эндпоинт /health возвращает статус healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    print("✅ Health check работает!")


def test_get_items_empty():
    """Тест: получение пустого списка товаров."""
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    print("✅ Получение списка товаров работает!")


def test_create_item():
    """Тест: создание нового товара."""
    item_data = {
        "name": "Test Product",
        "price": 99.99,
        "quantity": 5
    }
    response = client.post("/items/1", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["item"]["name"] == "Test Product"
    print("✅ Создание товара работает!")


def test_get_item():
    """Тест: получение товара по ID."""
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert "item" in data
    print("✅ Получение товара по ID работает!")


def test_delete_item():
    """Тест: удаление товара."""
    response = client.delete("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    print("✅ Удаление товара работает!")


def test_get_nonexistent_item():
    """Тест: запрос несуществующего товара."""
    response = client.get("/items/99999")
    assert response.status_code == 200
    data = response.json()
    assert "error" in data
    print("✅ Обработка несуществующего товара работает!")


def test_docs_available():
    """Тест: документация API доступна."""
    response = client.get("/docs")
    assert response.status_code == 200
    print("✅ Документация /docs доступна!")
