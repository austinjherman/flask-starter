import jwt
from functools import wraps
from app.user.model import User
from flask import current_app, request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return {'message': 'Token is missing.'}, 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            current_user = User.query.filter_by(uuid=data['uuid']).first()
        except Exception:
            return {'message': 'Token is invalid.'}, 401

        return f(current_user, *args, **kwargs)

    return decorated
