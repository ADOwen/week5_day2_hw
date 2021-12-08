from app import app
from flask import render_template
from livereload import server


@app.route('/')
def home():
    return render_template('index.html', my_title = 'Home', name = 'Allan', my_list= ['Allan','Mike','Chris',"Jay", "Booms"])

@app.route('/about')
def about():
    return render_template('about.html')

