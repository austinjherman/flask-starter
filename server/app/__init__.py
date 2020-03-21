import os
from flask import Flask
from flask_migrate import Migrate
from app.extensions import api, db
from flask_restful import Resource
from app.user.crud import UserListRoute, UserRoute


def create_app():
    app = Flask(__name__.split('.')[0])
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    Migrate(app, db)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(UserListRoute, '/users')
api.add_resource(UserRoute, '/users/<user_id>')


app = create_app()
