from app import my_app
from flask import render_template

@my_app.route('/')
def home():
    return render_template('index.html')

@my_app.route('/about')
def about():
    return render_template('about.html')

@my_app.route('/contact')
def contact():
    return render_template('contact.html')