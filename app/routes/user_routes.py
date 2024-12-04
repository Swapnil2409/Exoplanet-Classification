from flask import Blueprint, render_template, request, jsonify

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    """User login functionality."""
    if request.method == "POST":
        # Process login
        return jsonify({"message": "Login successful"})
    return render_template("login.html")

@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    """User registration functionality."""
    if request.method == "POST":
        # Process registration
        return jsonify({"message": "Registration successful"})
    return render_template("register.html")
