from flask import jsonify
from . import admin_blueprint
from middleware import requires_role, roles

@admin_blueprint.route('/')
@requires_role(roles['admin'])  # Only admins can access this route
def admin_dashboard():
    return jsonify({"message": "Welcome to the admin dashboard!"})

@admin_blueprint.route('/create', methods=['POST'])
@requires_role(roles['admin'])  # Only admins can access this route
def create_resource():
    return jsonify({"message": "Welcome to the admin dashboardfff!"})
