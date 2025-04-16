import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    PER_PAGE = os.environ.get("PER_PAGE", 10)


class DevConfig(Config):
    DEBUG = os.environ.get("FLASK_DEBUG", False)


class ProdConfig(Config):
    pass
