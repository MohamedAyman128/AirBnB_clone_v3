#!/usr/bin/python3
"""this is flask app"""

from flask import Flask, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """close the session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    '''return render_template'''
    data = {'error': 'Not found'}
    return jsonify(data), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
