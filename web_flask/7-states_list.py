#!/usr/bin/python3
"""A web application listening on 0.0.0.0:5000
    Routes:
        /states_list - Lists all State objects in a storage
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an html page with list of all States"""
    states = storage.all(State)
    return (render_template("7-states_list.html", states=states))


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
