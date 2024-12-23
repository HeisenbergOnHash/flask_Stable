from flask import Flask
from config import SECRET_KEY
from auth import auth_blueprint
from admin import admin_blueprint
from user import user_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/')
app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True)
