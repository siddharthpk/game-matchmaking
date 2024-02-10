from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import views from the views module
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
