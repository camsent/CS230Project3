# We use the __init__ name for our flask app because
#   this name is special for Python. This indicates that
#   the directory is a Python package. When an import 
#   occurs using the package, the __init__.py is
#   executed implicity

from flask import Flask

def create_app():
    app = Flask(__name__)

    # We do the imports for the Blueprints here to ensure that
    #   the Flask app is already created before we register the
    #   blueprint and its routes with Flask.
    from .routes import bp
    app.register_blueprint(bp)

    # Give the flask object to our "main" or entry point for the application.
    return app
