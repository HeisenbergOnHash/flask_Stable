from flask import Blueprint

# Create a Blueprint for admin-related routes
admin_blueprint = Blueprint('admin', __name__)

from .views import *  # Import views for the admin module
