from dotenv import load_dotenv
load_dotenv()
from flask_restful_api.app import create_app
from flask_restful_api.config import DevConfig

app = create_app(config_class=DevConfig)


if __name__ == '__main__':
    app.run()
