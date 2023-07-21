#!/usr/bin/python3
"""Starts a Flask web application
    Listening on 0.0.0.0:5000
    Routes:
        /: displays "Hello HBNB"
        /hbnb: displays "HBNB"
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    text = text.replace("_", " ")
    return ("C {}".format(escape(text)))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    text = text.replace("_", " ")
    return ("Python {}".format(escape(text)))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    return ("{} is a number".format(escape(n)))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
