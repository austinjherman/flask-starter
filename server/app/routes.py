from app.extensions import api
from app.auth.login import LoginController
from app.user.crud import UserListController, UserController


def register_routes():
    api.add_resource(UserListController, '/users')
    api.add_resource(UserController, '/users/<uuid>')
    api.add_resource(LoginController, '/login')
