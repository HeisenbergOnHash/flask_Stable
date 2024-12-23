from flask import Blueprint

# Create a Blueprint for user-related routes
user_blueprint = Blueprint('user', __name__)

from .views import *  # Import views for the user module
