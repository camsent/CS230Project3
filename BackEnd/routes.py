# This is a Flask Blueprint
#   This allows you to modularize your application.
#   If we only used our a single file for our application
#   like run or __init__.py for our program it makes it hard
#   to maintain it and when working in a group, you'll encounter
#   tons of merge conflicts when trying to commit changes.
from flask import Blueprint, jsonify, current_app

# A Flask blueprint minimally needs a unique name and the import_name.
#   The name is used to reference the blueprint via Flask functions
#   while the import_name helps to locate the blueprint and any resources
#   associated with it.
bp = Blueprint("main", __name__)

# This decorator is like the app.route, but is applied to the blueprint
#   object instead to hold the route. Everything else works mostly as
#   normal.
@bp.route("/hello")
def hello():
    return jsonify(message="Hello, Flask Factory!")
    

