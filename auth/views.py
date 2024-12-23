from flask import jsonify, request, make_response
from . import auth_blueprint
from middleware import create_token

@auth_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Example authentication (replace with actual logic)
    if username == 'admin' and password == 'admin_password':
        role = 'admin'
    elif username == 'user' and password == 'user_password':
        role = 'user'
    else:
        return jsonify({"message": "Invalid credentials!"}), 401
    
    # Generate JWT token for the user
    token = create_token(username, role)
    
    # Set the token in a secure HttpOnly cookie
    response = jsonify({"message": "Login successful!"})
    response.set_cookie('access_token', token, httponly=True, secure=True)
    return response


@auth_blueprint.route('/', methods=['GET'])
def base():

    # Set the token in a secure HttpOnly cookie
    response = jsonify({"message": "Login successful!"})

    return response
