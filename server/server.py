import flask
import json
import gunicorn
import logging
import flask_socketio
import os
from .routs import load_routs


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
app.secret_key = os.urandom(24)

def start_server(port=5000, host='127.0.0.1', debug=False):
    load_routs(app, socketio)
    app.run(port=port, host=host, debug=debug)


def stop_server():
    pass


def restart_server():
    pass