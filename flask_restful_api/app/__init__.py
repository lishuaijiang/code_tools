from flask import Flask

from flask_restful_api.app import extensions
from flask_restful_api.app import hooks as app_hooks
from flask_restful_api.app.api import v1
from flask_restful_api.app.api import v2
from flask_restful_api.app.api.v1 import hooks as v1_hooks


def create_app(config_class="flask_restful_api.config.DevConfig"):
    app = Flask(__name__)

    app.config.from_object(config_class)
    _init_extensions(app)
    _register_blueprints(app)
    _register_hooks(app)
    _register_commands(app)

    return app


def _init_extensions(app):
    """初始化各种扩展"""
    extensions.db.init_app(app)
    extensions.migrate.init_app(app, extensions.db)


def _register_blueprints(app):
    """注册所有蓝图"""
    app.register_blueprint(v1.v1_api)
    app.register_blueprint(v2.v2_api)


def _register_hooks(app):
    """注册钩子函数(请求时正序执行先应用后蓝图，响应时倒序执行先蓝图后应用)"""
    app_hooks.register_app_hooks(app)
    v1_hooks.register_v1_api_hooks(v1.v1_api)


def _register_commands(app):
    """注册 CLI 命令"""
    pass
