import json
from app.extensions import db
from app.user.model import User
from flask import request, Response
from marshmallow import ValidationError
from flask_restful import abort, Resource
from app.user.schema import users_schema, user_schema


def user_or_abort(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, message="User {} doesn't exist".format(user_id))
    return user


# User
# get, update, and delete a user
class UserRoute(Resource):

    def get(self, user_id):
        user = user_or_abort(user_id)
        return {
            'id': user.id,
            'email': user.email,
            'name': user.name
        }

    def delete(self, todo_id):
        pass
        # abort_if_todo_doesnt_exist(todo_id)
        # del TODOS[todo_id]
        # return '', 204

    def put(self, todo_id):
        pass
        # args = parser.parse_args()
        # task = {'task': args['task']}
        # TODOS[todo_id] = task
        # return task, 201


# Users
# get all users, create a new user
class UserListRoute(Resource):

    def get(self):
        all_users = User.query.all()
        return users_schema.dump(all_users)

    def post(self):

        try:
            user = user_schema.load(request.get_json())

        except ValidationError as err:
            msg = json.dumps({
                'message': err.messages,
                'valid': err.valid_data
            })
            return Response(msg, status=400, mimetype='application/json')

        exists = User.query.filter_by(email=user.email).first()
        if exists:
            return Response(json.dumps({
                'message': 'Email already registered.'
            }), status=400, mimetype='application/json')

        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user)
