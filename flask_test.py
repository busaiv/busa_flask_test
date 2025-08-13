from flask import Flask

my_app = Flask(__name__)

@my_app.route('/hello')
def hello():
    return 'Hello, world!'

@my_app.route('/info')
def info():
    return 'This is an informational page.'

@my_app.route('/calc/<num1>/<num2>')
def my_sum(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'The sum of {num1} and {num2} is {num1 + num2}.'
    except ValueError:
        return f'Incorrect value'

@my_app.route('/reverse/')
@my_app.route('/reverse/<data>')
def my_reverse(data=None):
    if data:
        return data[::-1]
    else:
        return 'Incorrect value'

@my_app.route('/user/<name>/<age>')
def user_welcome(name, age):
    try:
        if int(age) > 0:
            return f'Hello, {name}. You are {age} years old.'
        else:
            return 'Incorrect value'
    except ValueError:
        return f'Incorrect value'


if __name__ == '__main__':
    my_app.run(debug=True)