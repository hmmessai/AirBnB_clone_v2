#!/usr/bin/python3
"""Starts a Flask web application
    Route:
        /cities_by_states - displays cities within states
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """Display a HTML page with all States
    and the cities inside the State
    """
    states = storage.all(State)
    return (render_template("8-cities_by_states", states=states))
    

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
