from flask import Blueprint, request, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user

auth_bp = Blueprint('auth', __name__)

# Dummy user (replace with DB later)
class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {"test@example.com": {"password": "1234"}}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = users.get(email)
    if user and user["password"] == password:
        user_obj = User(id=email)
        login_user(user_obj)
        return jsonify({"message": "Logged in"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"}), 200

@auth_bp.route("/me", methods=["GET"])
def get_user():
    if current_user.is_authenticated:
        return jsonify({"email": current_user.id}), 200
    return jsonify({"email": None}), 200