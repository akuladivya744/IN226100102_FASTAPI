from fastapi import FastAPI

app = FastAPI()

# Products list
products = [
    {"id": 1, "name": "Laptop", "price": 50000, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 500, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Notebook", "price": 50, "category": "Stationery", "in_stock": False},
    {"id": 4, "name": "Pen", "price": 20, "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1500, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 3500, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 2500, "category": "Electronics", "in_stock": False}
]

# 1️⃣ Get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


# 2️⃣ Filter products by category
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    result = []

    for p in products:
        if p["category"] == category_name:
            result.append(p)

    return result


# 3️⃣ Show only in-stock products
@app.get("/products/instock")
def get_instock_products():

    result = []

    for p in products:
        if p["in_stock"] == True:
            result.append(p)

    return {
        "in_stock_products": result,
        "count": len(result)
    }


# 4️⃣ Store summary
@app.get("/products/summary")
def get_summary():

    total_products = len(products)
    instock_count = 0
    categories = []

    for p in products:

        if p["in_stock"] == True:
            instock_count += 1

        if p["category"] not in categories:
            categories.append(p["category"])

    return {
        "total_products": total_products,
        "in_stock_products": instock_count,
        "categories": categories
    }


# 5️⃣ Search products
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    result = []

    for p in products:
        if keyword.lower() in p["name"].lower():
            result.append(p)

    return result


# 6️⃣ Cheapest and most expensive product
@app.get("/products/deals")
def get_best_and_premium():

    cheapest = products[0]
    expensive = products[0]

    for p in products:

        if p["price"] < cheapest["price"]:
            cheapest = p

        if p["price"] > expensive["price"]:
            expensive = p

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }