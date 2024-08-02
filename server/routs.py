import flask
import flask_socketio
import gunicorn
import logging
import json
import os



def load_routs(app, socketio):
    with open('server/routes.json', 'r') as f:
        routes = json.load(f)

    for route in routes:
        if route == 'socket':
            for socket in routes[route]:
                socketio.on_namespace(routes[route][socket])
        else:
            app.add_url_rule(routes[route]['path'], route, routes[route]['function'])

    