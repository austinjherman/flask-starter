import uuid
import json
from app.extensions import db
from app.user.model import User
from flask import request, Response
from marshmallow import ValidationError
from flask_restful import abort, Resource
from app.auth.token_required import token_required
from app.user.schema import users_schema, user_schema


def user_or_abort(uuid):
    user = User.query.filter_by(uuid=uuid).first()
    if not user:
        abort(404, message="User {} doesn't exist".format(uuid))
    return user


# User
# get, update, and delete a user
class UserController(Resource):

    @token_required
    def get(self, current_user, uuid):
        user = user_or_abort(uuid)
        return user_schema.dump(user)

    @token_required
    def delete(self, current_user, uuid):
        user = user_or_abort(uuid)
        db.session.delete(user)
        db.session.commit()
        return user_schema.dump(user)

    @token_required
    def put(self, current_user, uuid):

        user = User.query.filter_by(id=uuid).first()
        if not user:
            return Response(json.dumps({
                'message': 'User with id {} does not exist'.format(uuid)
            }), status=400, mimetype='application/json')

        try:
            json_input = user_schema.load(
                request.get_json(), partial=True
            )

        except ValidationError as err:
            msg = json.dumps({
                'message': err.messages,
                'valid': err.valid_data
            })
            return Response(msg, status=400, mimetype='application/json')

        for prop, value in json_input.__dict__.items():

            if prop == 'email':
                exists = User.query.filter_by(email=value).first()
                if exists:
                    return Response(json.dumps({
                        'message': 'Email already registered.'
                    }), status=400, mimetype='application/json')
                setattr(user, prop, value)

            if prop == 'password':
                setattr(user, prop, User.hash_password(user.password))

        db.session.commit()
        return user_schema.dump(user)


# Users
# get all users, create a new user
class UserListController(Resource):

    @token_required
    def get(self, current_user):
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

        user.uuid = uuid.uuid4()
        user.password = User.hash_password(user.password)

        db.session.add(user)
        db.session.commit()

        return Response(
            user_schema.dumps(user), status=201, mimetype='application/json'
        )
