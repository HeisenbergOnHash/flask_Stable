from flask import Blueprint

# Create a Blueprint for authentication
auth_blueprint = Blueprint('auth', __name__)

from .views import *  # Import views for the auth module
