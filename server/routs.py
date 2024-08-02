import flask
import flask_socketio
import gunicorn
import logging
import json
import os



def load_routs(app, socketio):
    with open('server/routes.json', 'r') as f:
        routes = json.load(f)

    