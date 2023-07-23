#!/usr/bin/python3
"""Starts a Flask web app
    Route:
        /states - display states
        /states/<id> - display state with the id
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """Displays a HTML page"""
    states = storage.all(State)
    return (render_template("9-states.html", id=id, states=states))


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
