import pytest
from flask import Flask
from app import app  # Импортируем приложение Flask

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_download_file(client):
    # Отправляем GET запрос на маршрут скачивания
    response = client.get('/download')
    
    # Проверяем, что запрос прошел успешно
    assert response.status_code == 200

    # Проверяем, что содержимое файла — это "Hello World!"
    assert response.data == b'Hello World!'

    # Проверяем, что заголовок для скачивания файла корректный
    assert response.headers['Content-Disposition'] == 'attachment; filename=hello.txt'
