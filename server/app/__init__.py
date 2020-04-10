import os
from flask import Flask
from app.routes import register_routes
from app.extensions import api, db, ma, migrate, bcrypt


def create_app():
    app = Flask(__name__.split('.')[0])
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)


register_routes()
app = create_app()
