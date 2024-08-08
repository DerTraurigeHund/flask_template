import flask
import json
import gunicorn
import logging
import flask_socketio
import os
from .routs import load_routs


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
app.secret_key = "this is a super secret key"
app.template_folder = 'client/html'

def start_server():
    load_routs(app, socketio)
    socketio.run(app=app)


def stop_server():
    pass


def restart_server():
    pass