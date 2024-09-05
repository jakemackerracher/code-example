from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from base import db, bcrypt
from models import User
from schemas.user import UserResponseSchema
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import not_, and_

users_bp = Blueprint('users', __name__)

@users_bp.route("/")
@login_required
def get_users():
    # Ensure only admins can see all users
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 401

    # Find and return all users
    users = User.query.all()
    user_response_schema = UserResponseSchema(many=True)
    result = user_response_schema.dump(users)
    return jsonify(result)

@users_bp.route("/", methods=['POST'])
def create_user():
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

    # Check the database transaction was successful
    try:
        # Save the model
        db.session.add(user)
        db.session.commit()
    except SQLAlchemyError as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({'error': e}), 500

    return jsonify(), 201

@users_bp.route("/<string:user_id>")
@login_required
def get_user(user_id):
    # Ensure only admins or user (self) can view user
    if not current_user.is_admin and current_user.id != user_id :
        return jsonify({'error': 'Unauthorized'}), 401

    # Ensure user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Process user response through user schema
    user_response_schema = UserResponseSchema()
    result = user_response_schema.dump(user)
    return jsonify(result)

@users_bp.route("/<string:user_id>", methods=['PUT', 'PATCH'])
@login_required
def update_user(user_id):
    # Ensure only admins or user (self) can update user
    if not current_user.is_admin and current_user.id != user_id :
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Ensure user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Handle json bundle
    data = request.get_json()
    # Update attributes based on the request data
    for key, value in data.items():
        # Handling keys in the array below further down
        if key in ["email", "password", "is_admin"]:
            continue
        setattr(user, key, value)

    # Check if email is being updated
    if 'email' in data:
        # Check if user already exists
        email = data.get('email')
        email_in_use = User.query.filter(
            and_(User.email == email, not_(User.id == current_user.id))
        ).first() is not None
        if email_in_use:
            return jsonify({'error': 'Email already in use'}), 409
        user.email = email

    # Check if password is being updated
    if 'password' in data:
        # Encrypt password given
        password = data.get('password')
        password_hash = bcrypt.generate_password_hash(password)

        # Ask for current password if not admin
        if not current_user.is_admin:
            if "current_password" not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            current_password = data.get('current_password')
            current_password_matches = bcrypt.check_password_hash(user.password, current_password)
            if not current_password_matches:
                return jsonify({'error': 'Invalid credentials'}), 404
        user.password = password_hash

    # Check if is_admin is being updated
    if 'is_admin' in data:
        # Block not admins from updating this field
        if not current_user.is_admin:
            return jsonify({'error': 'Unauthorized'}), 401
        user.is_admin = data.get('is_admin', user.is_admin)

    # Check the database transaction was successful
    try:
        # Save the updated model
        db.session.commit()
    except SQLAlchemyError as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({'error': e}), 500

    return jsonify(), 204

@users_bp.route("/<string:user_id>", methods=['DELETE'])
@login_required
def delete_user(user_id):
    # Ensure only admins or user (self) can delete user
    if not current_user.is_admin and current_user.id != user_id :
        return jsonify({'error': 'Unauthorized'}), 401

    # Ensure user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Check the database transaction was successful
    try:
        # Save the updated model
        db.session.delete(user)
        db.session.commit()
    except SQLAlchemyError as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({'error': e}), 500

    return jsonify(), 204