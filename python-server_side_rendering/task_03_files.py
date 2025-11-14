from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data from appropriate source
    if source == 'json':
        products_list = read_json_file()
    else:  # csv
        products_list = read_csv_file()
    
    # Filter by id if provided
    if product_id is not None:
        filtered_products = [p for p in products_list if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products_list = filtered_products
    
    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
