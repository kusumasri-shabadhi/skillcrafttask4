import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("div", class_="product")

    with open("products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        
        writer.writerow(["Product Name", "Price", "Rating"])

        
        for product in products:
            name = product.find("h2", class_="product-name")
            price = product.find("span", class_="price")
            rating = product.find("span", class_="rating")

            writer.writerow([
                name.text.strip() if name else "N/A",
                price.text.strip() if price else "N/A",
                rating.text.strip() if rating else "N/A"
            ])

    print("Data successfully saved to products.csv")

else:
    print("Failed to retrieve webpage:", response.status_code)
    