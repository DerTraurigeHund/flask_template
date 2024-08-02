import flask
import flask_socketio
import gunicorn
import logging
import json
import os
import colorama
from config.session import get_session_permissions

GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED
RESET = colorama.Fore.RESET

def load_routs(app, socketio):
    with open('server/routes.json', 'r') as f:
        routes = json.load(f)

    for route in routes:
        if route == 'socket':
            for socket in routes[route]:
                try:
                    name = routes[route][socket]['name']
                    description = routes[route][socket]['description']
                    function = eval(routes[route][socket]['function'])

                    socketio.on_event(socket, function)

                    print(GREEN + f'Socket {name} loaded' + RESET)

                except Exception as e:
                    print(RED + f'Socket {name} not loaded: {str(e)}' + RESET)
        elif route == 'html':
            for html in routes[route]:
                try:
                    name = routes[route][html]['name']
                    description = routes[route][html]['description']
                    file = routes[route][html]['file']
                    premission = routes[route][html]['required_permissions']
                    dynamic = routes[route][html]['daynamic']

                    if dynamic == [False]:
                        @app.route(html)
                        def {html}():

