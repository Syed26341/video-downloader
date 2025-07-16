# utils/response.py

from flask import jsonify

def success_response(data=None, message="Success"):
    return jsonify({
        'status': 'success',
        'message': message,
        'data': data
    }), 200

def error_response(message="Something went wrong", status_code=400):
    return jsonify({
        'status': 'error',
        'message': message,
        'data': None
    }), status_code
