from flask import jsonify, request
from routes.location import main_routes

def bootstrap_routes(app):
    @app.before_request
    def before_request():
        if request.method == 'POST':
            if request.form or request.data:
                return

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({}), 200


    @app.route('/status', methods=['GET'])
    def healthcheck():
        return jsonify(status=200)

    main_routes(app)