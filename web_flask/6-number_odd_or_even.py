#!/usr/bin/python3
"""Starts a flask web application
"""
from flask import Flask, render_template

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


@app.route('/number_template/<int:n>')
def number_template(n):
    """_summary_"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
