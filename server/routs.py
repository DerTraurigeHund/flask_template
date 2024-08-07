import flask
import flask_socketio
import gunicorn
import logging
import json
import os
import colorama
from config.permission import check_permissions

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
                if routes[route][html]['daynamic'] == [False]:
                    try:
                        needed_permissions = routes[route][html]['required_permissions']
                        template = routes[route][html]['file']
                        func = f"""
                        def {routes[route][html]['name']}(path = None):
                            if check_permissions({needed_permissions}):
                                return flask.render_template('{template}')
                            else:
                                return flask.redirect('/error/403')
                        """

                        exec(func)

                        app.add_url_rule(html, html, eval(html))

                        print(GREEN + f'Html {routes[route][html]["name"]} loaded' + RESET)

                    except Exception as e:  
                        print(RED + f'Html {routes[route][html]["name"]} not loaded: {str(e)}' + RESET)

                elif routes[route][html]['daynamic'] == [True]:
                    pass

                else:
                    pass

        elif route == 'api':
            for api in routes[route]:
                try:
                    name = routes[route][api]['name']
                    description = routes[route][api]['description']
                    function = eval(routes[route][api]['function'])

                    app.add_url_rule(api, api, function)

                    print(GREEN + f'Api {name} loaded' + RESET)

                except Exception as e:
                    print(RED + f'Api {name} not loaded: {str(e)}' + RESET)

        elif route == 'other':
            for other in routes[route]:
                try:
                    name = routes[route][other]['name']
                    description = routes[route][other]['description']
                    function = eval(routes[route][other]['function'])

                    app.add_url_rule(other, other, function)

                    print(GREEN + f'Other {name} loaded' + RESET)

                except Exception as e:
                    print(RED + f'Other {name} not loaded: {str(e)}' + RESET)