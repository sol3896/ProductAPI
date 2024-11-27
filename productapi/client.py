import requests

BASE_URL = "http://127.0.0.1:8000/api/products"

# Add a new product
product_data = {
    "name": "Smartphone",
    "description": "An Android smartphone with excellent performance.",
    "price": 499.99
}
response = requests.post(f"{BASE_URL}/create/", json=product_data)
if response.status_code == 201:
    print("Product created:", response.json())
else:
    print("Error creating product:", response.json())

# Retrieve all products
response = requests.get(BASE_URL + "/")
if response.status_code == 200:
    print("Product list:", response.json())
else:
    print("Error fetching products:", response.json())
