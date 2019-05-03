from beers.settings import app_config
from flask import Flask
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)

    # Cors Config
    CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

    app.config.from_object(app_config[config_name])

    # Initialize Extensions
    register_extensions(app)

    # Initialize Blueprints
    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register Blueprints"""
    from beers.app.blueprints.api.beers import resource as beer_api
    from beers.app.blueprints.api.beers_list import resource as list_beers_api
    from beers.app.blueprints.api.ingredients import resource as ingredients_api

    beer_api.init_app(app)
    list_beers_api.init_app(app)
    ingredients_api.init_app(app)
    return app


def register_extensions(app):
    """Register extensions."""
    from beers.app.ext.db import db
    from beers.app.ext.migrate import migrate

    db.init_app(app)
    migrate.init_app(app, db)
    return app
