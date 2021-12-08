from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('index.html', my_title = 'Home', my_list= ['Games','Electronics','Accesories', 'And More!'])

@app.route('/products')
def products():
    return render_template('products.html')

