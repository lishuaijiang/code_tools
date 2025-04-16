from flask import Blueprint, jsonify

user_api = Blueprint('user_api', __name__, url_prefix='/users')


@user_api.route('')
def get_users():
    fake_users = [
        {"id": 1, "name": "Alice", "gender": "female"},
        {"id": 2, "name": "Bob", "gender": "male"},
        {"id": 3, "name": "Charlie", "gender": "male"},
    ]
    return jsonify(fake_users)
