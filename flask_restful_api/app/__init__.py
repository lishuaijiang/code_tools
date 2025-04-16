from flask import Flask


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    from flask_restful_api.app.api.v1 import v1_api
    from flask_restful_api.app.api.v2 import v2_api

    app.register_blueprint(v1_api)
    app.register_blueprint(v2_api)

    return app
