from flask import Blueprint

v1_api = Blueprint('v1_api', __name__, url_prefix='/api/v1')

# 注册子蓝图
from flask_restful_api.app.api.v1.user import user_api
v1_api.register_blueprint(user_api)
