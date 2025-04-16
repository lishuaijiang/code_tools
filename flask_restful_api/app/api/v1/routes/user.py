from flask import Blueprint
from flask import current_app
from flask import request
from flask import jsonify

from flask_restful_api.app.models.user import User
from flask_restful_api.app.schemas.user import UserSchema

user_api = Blueprint('user_api', __name__, url_prefix='/users')


@user_api.route('')
def get_users():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', current_app.config['PER_PAGE']))
    sort_by = request.args.get('sort_by', 'created_at')
    order = request.args.get('order', 'desc')

    if page < 1 or per_page < 1:
        return jsonify({'error': 'Invalid pagination parameters'}), 400

    count = User.query.count()
    query = User.query
    if hasattr(User, sort_by):
        sort_column = getattr(User, sort_by)
        _order = sort_column.asc() if order == 'asc' else sort_column.desc()
        query = query.order_by(_order)

    pagination = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    users = UserSchema(many=True).dump(pagination.items)
    return jsonify({'users': users, 'total': count}), 200


@user_api.route('/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    user = UserSchema().dump(user)
    return jsonify({'user': user}), 200


@user_api.route('/', methods=['POST'])
def create_user():
    pass


@user_api.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    pass
