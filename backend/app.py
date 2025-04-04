from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from auth import auth_bp, User

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Use env vars in production
app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE=True  # required for cross-origin cookies
)
CORS(app, supports_credentials=True, origins=["http://localhost:3000/"])

# Session-based login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Register Blueprints
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)

