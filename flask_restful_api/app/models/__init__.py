from datetime import datetime
from flask_restful_api.app.extensions import db


class BaseModel(db.Model):
    __abstract__ = True  # 声明为抽象类，SQLAlchemy 不会为它创建表

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    deleted_at = db.Column(db.DateTime, default=datetime.now)
