# check, if requirements are installed
try:
    import flask
    import flask_socketio
    import gunicorn
    import logging
    import json
    import argparse
except ImportError:
    print('Please install the required packages: pip install -r requirements.txt')
    exit()

import flask.sansio
from .server.server import start_server, stop_server, restart_server
import os


# Parse arguments
parser = argparse.ArgumentParser(description='Example script with arguments')

# Add arguments
parser.add_argument('-start', action='store_true', help='Restart the application')
parser.add_argument('-debug', type=bool, default=False, help='Enable debugging mode')
parser.add_argument('-restart', action='store_true', help='Restart the application')
parser.add_argument('-stop', action='store_true', help='Stop the application')
parser.add_argument('-port', type=int, default=5000, help='Server port')
parser.add_argument('-host', type=str, default='127.0.0.1', help='Server host')

# Parse arguments
args = parser.parse_args()

actions = {
    'start': start_server,
    'stop': stop_server,
    'restart': restart_server
}

for action in actions:
    if getattr(args, action):
        actions[action](args)