from flask import jsonify
from . import user_blueprint
from middleware import requires_role, roles

@user_blueprint.route('/')
@requires_role(roles['user'])  # Only users can access this route
def user_dashboard():
    return jsonify({"message": "Welcome to the user dashboard!"})
