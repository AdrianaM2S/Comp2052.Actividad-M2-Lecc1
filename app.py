# Import necessary modules for Flask and template rendering
from flask import Flask, render_template 

# Create an instance of the Flask application
app = Flask(__name__)  

# Define the route for the homepage
@app.route('/')
def index():
    data = {
        "title": "Main Page",
        "message": "Welcome to my Flask application."
    }
    # Render the index.html template with the provided data
    return render_template('index.html', data=data) 

# Define the route for the commissions page
@app.route('/commissions')
def commissions():
    data = {
        "title": "List of commissions",
        "message": "This is the list of art commissions that are yet to be done."
    }
    # Render the commissions.html template with the provided data
    return render_template('commissions.html', data=data)

# Define the route for the products page
@app.route('/products')
def products():
    data = {
        "title": "Product inventory",  #
        "products": 
        [  # List of available products with details
            {"item": "Flower Pins", "price": 5.00, "inStock": 25},
            {"item": "Animal Keychains", "price": 12.00, "inStock": 50},
            {"item": "Character Prints", "price": 10.00, "inStock": 62}
        ]
    }
    # Render the products.html template with the provided data
    return render_template('products.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)