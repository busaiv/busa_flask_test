from app import my_app
from flask import render_template, request, redirect, url_for

@my_app.route('/')
def home():
    return render_template('home.html')

@my_app.route('/about')
def about():
    return render_template('about.html')

@my_app.route('/contact')
def contact():
    return render_template('contact.html')

@my_app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('result.html', name=name, email=email, message=message)
    else:
        return redirect(url_for('contact'))
