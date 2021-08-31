from flask import (
    Blueprint,
    jsonify, 
    request,
    make_response,
)
from werkzeug.exceptions import (
    BadRequest, 
    InternalServerError, 
    NotFound, 
    Unauthorized
)
from todo.db import get_db
from .schemas import TodoSchema
from .models import Todo
from .utils import custom_response
from . import db

bp = Blueprint('todo', __name__, url_prefix='/todos')
todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
DB = db.get_db()


@bp.route('', methods=['GET'])
def get_all_todo():
    all_todos = Todo.query.all()
    results = todos_schema.dump(all_todos)
    return jsonify(results), 200

@bp.route('todo/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    todo = Todo.query.get(id)
    if todo:
        return todo_schema.jsonify(todo), 200
    return custom_response({
        "message":"Not found"
    }, 404)

@bp.route('todo/create', methods=['POST'])
def create_todo():
    new_todo = Todo(
        request.json['title'],
        request.json['description']
    )
    try:
        DB.session.add(new_todo)
        DB.session.commit()
        response = todo_schema.jsonify(new_todo)
        return response, 201
    except Exception as e:
        DB.session.rollback()
        return custom_response({
            "message":"Could not created",
            "exception": e
        }, 409)

@bp.route('todo/update/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get(id)
    todo.title = request.json['title']
    todo.description = request.json['description']
    try:
        DB.session.commit()
        return todo_schema.jsonify(todo), 200
    except Exception:
        DB.session.rollback()
        return custom_response({
            "message":"Could not updted"
        }, 409)

@bp.route('todo/delete/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get(id)
    try:
        DB.session.delete(todo)
        DB.session.commit()
        return custom_response({
            "message":"Deleted"
        }, 200)
    except Exception:
        DB.session.rollback()
        return custom_response({
            "message":"Could not deleted"
        }, 409)

@bp.errorhandler(BadRequest)
def handle_bad_request(e):
    return make_response(jsonify({'error': 'Misunderstood'}), 400)

@bp.errorhandler(Unauthorized)
def handle_401_error(e):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)
    
@bp.errorhandler(InternalServerError)
def handle_server_error(e):
    return make_response(jsonify({'error': 'Internl server error'}), 500)

@bp.errorhandler(NotFound)
def handle_not_found(e):
    return make_response(jsonify({'error': 'Not found'}), 404)

@bp.route('/db', methods=['GET'])
def db_test():
    print(get_db())
    return f'{get_db()}'

@bp.route('/dockertest', methods=['GET'])
def dockertest():
    return 'Hi from docker'