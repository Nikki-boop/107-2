from flask import Flask, request
import json

app = Flask(__name__)


@app.get("/")
def hello__world():
    return "Hello World Finally"

@app.get("/api/version")
def version():
    version={"name": "products-api", "version": 1}
    return json.dumps (version)


products = []

@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f"New product: {product}")

    products.append(product)
    return json.dumps(product)

@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"index: {index}")

    if index >=0 and index <len(products):
        deleted_product = products.pop(index)
        return json.dumps (deleted_product)
    else:
        # return "That index does not exist"

    return "Deleting"


app.run(debug=True)