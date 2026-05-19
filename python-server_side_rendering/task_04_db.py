#!/usr/bin/python3
"""
Flask app that reads product data from JSON, CSV, or SQLite database.
"""

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """
    Read products from products.json.
    """
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv_file():
    """
    Read products from products.csv.
    """
    products = []

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)

    return products


def read_sql_file():
    """
    Read products from SQLite database.
    """
    products = []

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })

    conn.close()

    return products


@app.route("/products")
def products():
    """
    Display products from JSON, CSV, or SQL source.
    """
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            products_list = read_json_file()
        elif source == "csv":
            products_list = read_csv_file()
        elif source == "sql":
            products_list = read_sql_file()
        else:
            return render_template(
                "product_display.html",
                products=[],
                error="Wrong source"
            )

        if product_id:
            product_id = int(product_id)

            products_list = [
                product for product in products_list
                if int(product["id"]) == product_id
            ]

            if not products_list:
                return render_template(
                    "product_display.html",
                    products=[],
                    error="Product not found"
                )

        return render_template(
            "product_display.html",
            products=products_list,
            error=None
        )

    except sqlite3.Error:
        return render_template(
            "product_display.html",
            products=[],
            error="Database error"
        )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
