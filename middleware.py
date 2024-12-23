import jwt
from functools import wraps
from flask import request, jsonify
from config import SECRET_KEY
from datetime import datetime, timedelta

# Example roles
roles = {
    'admin': 'admin',
    'user': 'user'
}

# Function to create JWT token
def create_token(username, role):
    expiration = datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
    payload = {
        'username': username,
        'role': role,
        'exp': expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


# Function to decode the JWT token and get user info
def decode_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Decorator for role-based access control
def requires_role(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.cookies.get('access_token')  # Get token from cookies (or request header)
            if not token:
                return jsonify({"message": "Token is missing!"}), 403

            # Decode the token and extract the user role
            user_info = decode_token(token)
            if not user_info:
                return jsonify({"message": "Invalid token!"}), 401

            user_role = user_info.get('role')
            if user_role != required_role:
                return jsonify({"message": "You do not have the necessary permissions!"}), 403

            # Proceed to the actual route handler
            return f(*args, **kwargs)

        return decorated_function
    return decorator
