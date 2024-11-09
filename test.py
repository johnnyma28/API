from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

@app.get("/products")
def getProducts():
    result = cursor.execute('''SELECT * FROM products''')
    data = result.fetchall()
    print(data)  # This will print all 1000 records
    conn.commit()
    
    # Initialize an empty list to store all product dictionaries
    product_list = []
    
    # Loop through the data and append each item as a dictionary to product_list
    for item in data:
        print(item)  # Prints each individual item
        product = {
            "id": item[0],
            "title": item[1],
            "price": item[5],
            "description": item[2],
            "category": "men's clothing",
            "image": item[4],
            "rating": {
                "rate": 3.9,
                "count": 120
            }
        }
        product_list.append(product)  # Append each product to the list
    
    return jsonify(product_list)

if __name__ == '__main__':  # Make sure this is '__main__', not '_main_'
    app.run(debug=True, port=5000)
