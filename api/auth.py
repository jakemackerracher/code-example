from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from base import db, bcrypt
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # Logout current user if exists
    if current_user is not None:
        user_logged_out = logout_user()
        if not user_logged_out:
            return jsonify({'error': 'Logout current user failed'}), 500
        
    # Handle json bundle
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Validate the data
    if not name or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Check if user already exists
    user_exists = User.query.filter_by(email=email).first() is not None
    if user_exists:
        return jsonify({'error': 'User already registered'}), 409

    # Encrypt password and create user model
    password_hash = bcrypt.generate_password_hash(password)
    user = User(name=name, email=email, password=password_hash)
    db.session.add(user)
    db.session.commit()

    # Create user session
    login_user(user)

    return jsonify(), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    # Logout current user if exists
    if current_user is not None:
        user_logged_out = logout_user()
        if not user_logged_out:
            return jsonify({'error': 'Logout current user failed'}), 500

    # Handle json bundle
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validate the data
    if not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Find the user model and check it exists
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 404

    # Check that the password provided matches one against user model
    password_matches = bcrypt.check_password_hash(user.password, password)
    if not password_matches:
        return jsonify({'error': 'Invalid credentials'}), 404

    # Create user session
    user_logged_in = login_user(user)
    if not user_logged_in:
        return jsonify({'error': 'Login failed'}), 500

    return jsonify(), 204

@auth_bp.route("/logout")
@login_required
def logout():
    # Destroy user session
    user_logged_out = logout_user()
    if not user_logged_out:
        return jsonify({'error': 'Logout failed'}), 500
    return jsonify(), 204

@auth_bp.route("/user")
@login_required
def user():
    return jsonify({
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }), 200