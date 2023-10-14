from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:text>')
def print_string(text):
    return text

@app.route('/count/<int:num>')
def count(num):
    numbers = "\n".join(str(i) for i in range(1, num + 1))
    return numbers

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return f"Result: {num1} {operation} {num2} = {result}"


