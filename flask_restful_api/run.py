from dotenv import load_dotenv
load_dotenv()
from flask_restful_api.app import create_app

app = create_app()


if __name__ == '__main__':
    app.run()
