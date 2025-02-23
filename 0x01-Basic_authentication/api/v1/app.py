#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
if AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def handle_401_error(error):
    """
    Error handler for 401 Unauthorized error
    Args:
      - error: The error object

    Returns:
      - A JSON response with an error message and status code 401
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def handle_403_error(error):
    """
    Error handler for 403 Forbidden error
    Args:
      - error: The error object

    Returns:
      - A JSON response with an error message and status code 403
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request() -> None:
    '''before_request method'''
    if not auth:
        return

    paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    req = auth.require_auth(request.path, paths)
    if req:
        if not auth.authorization_header(request):
            abort(401)
        if not auth.current_user(request):
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
