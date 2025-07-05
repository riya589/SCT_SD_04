
import requests
import pandas as pd

def get_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()

    products = []
    for item in data:
        products.append({
            "title": item["title"],
            "price": item["price"],
            "rating": item["rating"]["rate"]
        })

    # Save to CSV
    df = pd.DataFrame(products)
    df.to_csv("data/products.csv", index=False)

    return products
