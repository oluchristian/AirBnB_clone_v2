#!/usr/bin/python3
"""Starts a flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """_summary_"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """_summary_
    """
    return "HBNB"


@app.route('/c/<text>')
def c_with_params(text):
    """_summary_"""
    text_with_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_with_no_underscore)


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_with_params(text):
    """Displays python followed by the value of text"""
    text_with_no_underscore = text.replace('_', ' ')
    return "Python {}".format(text_with_no_underscore)


@app.route('/number/<int:n>')
def number(n):
    """returns a number"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
