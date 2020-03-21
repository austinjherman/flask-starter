from app.user.model import User
from flask_restful import reqparse, abort, Resource


def user_or_abort(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, message="User {} doesn't exist".format(user_id))
    return user


parser = reqparse.RequestParser()
parser.add_argument('email', type=str, help='The user\'s email.')
parser.add_argument('name', type=str, help='The user\'s name.')
parser.add_argument('password', type=str, help='The user\'s password.')


# Todo
# shows a single todo item and lets you delete a todo item
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


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class UserListRoute(Resource):
    def get(self):
        return User.query.all()

    def post(self):
        pass
        # args = parser.parse_args()
        # todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        # todo_id = 'todo%i' % todo_id
        # TODOS[todo_id] = {'task': args['task']}
        # return TODOS[todo_id], 201
