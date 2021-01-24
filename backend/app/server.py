import os
from flask import Flask
from flask_cors import CORS

import handlers.baseroutes as routes


def create_server(test_config=None):
    app = Flask(__name__)
    CORS(app)

    if test_config is None:
        app.config.from_object(os.environ['APP_SETTINGS'])
    else:
        app.config.from_object(test_config)

    routes.bootstrap_routes(app)
    return app


def run_server(app):
    app.run(host="0.0.0.0", debug=app.config['DEBUG'])


def init(*args):
    flask_app = create_server()
    if __name__ == '__main__':
        run_server(flask_app)
    return flask_app


if os.environ.get('TESTING_MODE') != "True":
    init()
