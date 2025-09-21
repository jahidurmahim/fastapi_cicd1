from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Book Management System"}

def test_add_product():
    response = client.post("/book", json={
        "id": 101,
        "name": "Laptop",
        "description": "Gaming Laptop",
        "isAvailable": True
    })
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Laptop"

def test_get_products():
    response = client.get("/book")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

def test_update_product():
    response = client.put("/book/101", json={
        "id": 101,
        "name": "Laptop Updated",
        "description": "Updated Gaming Laptop",
        "isAvailable": False
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop Updated"

def test_delete_product():
    response = client.delete("/book/101")
    assert response.status_code == 200
    assert "deleted successfully" in response.json()["message"]

def test_delete_product_not_found():
    response = client.delete("/book/999")
    assert response.status_code == 200
    assert response.json() == {"error": "Book not found, deletion failed"}
