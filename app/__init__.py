from flask import Flask
from .routes.main import main_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint, url_prefix='/')

    return app