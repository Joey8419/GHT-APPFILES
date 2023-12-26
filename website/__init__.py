from flask import Flask


# Define a function:
def create_app():
    # This is how flask is initialized; __name__ represents the name of the file that was run:
    app = Flask(__name__)
    # config variable encrypts and secures the cookies and session data related to the website:
    app.config['SECRET_KEY'] = 'GHT APP'


# Blueprints must be registered in this file:
    from .views import views
    from .auth import auth

    # Register the blueprints:
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
