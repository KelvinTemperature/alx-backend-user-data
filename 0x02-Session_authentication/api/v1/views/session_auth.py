#!/usr/bin/env python3
"""Handles All routes for session authentication
"""
import os
from typing import Tuple
from flask import abort, jsonify, request

from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> Tuple[str, int]:
    """method to handle session login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or len(email.strip()) == 0:
        return jsonify({ "error": "email missing" }), 400
    if password is None or len(password.strip()) == 0:
        return jsonify({ "error": "password missing" }), 400
    
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({ "error": "no user found for this email" }), 404
    if len(users) <= 0:
        return jsonify({ "error": "no user found for this email" }), 404

    if users[0].is_valid_password(password) is False:
        return jsonify({ "error": "no user found for this email" }), 404

    from api.v1.app import auth
    session_id = auth.create_session(getattr(users[0], 'id'))
    res = jsonify(users[0].to_json())
    res.set_cookie(os.getenv('SESSION_NAME', session_id))
    return res

@app_views.route(
    'auth_session/logout', methods=['DELETE'], strict_slashes=False)
def session_logout() -> Tuple[str, int]:
    """route to handle logout
    """
    from api.v1.app import auth
    is_destroyed = auth.destroy_session(request)
    if not is_destroyed:
        abort(404)
    return jsonify({}), 200
