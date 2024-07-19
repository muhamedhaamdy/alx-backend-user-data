#!/usr/bin/env python3
'''flask app'''
from flask import Flask, jsonify, request, abort
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    ''' return json payload '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register():
    ''' register a user '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)

# @app.route('/sessions', methods=['POST'], strict_slashes=False)
# def login():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     try:
#         if AUTH.valid_login(email, password):
#             session_id = AUTH.create_session(email)
#             response = jsonify({"email": email, "message": "logged in"})
#             response.set_cookie('session_id', session_id)
#             return response
#         else:
#             abort(401)
#     except NoResultFound:
#         return jsonify({"message": "user not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
