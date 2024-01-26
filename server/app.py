#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''displays "Python Operations with Flask Routing and Views" in h1 in browser.'''
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_text(route):
    '''displays text of route in browser.'''
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):

    if operation == '+':
        return str(int(num1) + int(num2))
    elif operation == '-':
        return str(int(num1) - int(num2))
    elif operation == '*':
        return str(int(num1) * int(num2))
    elif operation == 'div':
        return str(int(num1) / int(num2))
    elif operation == '%':
        return str(int(num1) % int(num2))
    
    return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
