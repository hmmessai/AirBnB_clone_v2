#!/usr/bin/python3
"""Starts a Flask web application
    Listening on 0.0.0.0:5000
    Routes:
        /: displays "Hello HBNB"
        /hbnb: displays "HBNB"
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
