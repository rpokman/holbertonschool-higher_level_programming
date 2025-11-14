from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file():
    """Read and return data from products.json file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_file():
    """Read and return data from products.csv file."""
    try:
        products = []
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except FileNotFoundError:
        return []
    except (ValueError, KeyError):
        return []

def read_sql_database():
    """Read and return data from products.db SQLite database."""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data from appropriate source
    if source == 'json':
        products_list = read_json_file()
    elif source == 'csv':
        products_list = read_csv_file()
    else:  # sql
        products_list = read_sql_database()
    
    # Filter by id if provided
    if product_id is not None:
        filtered_products = [p for p in products_list if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products_list = filtered_products
    
    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
