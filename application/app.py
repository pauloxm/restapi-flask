from flask import request, jsonify, json
from .db import db
from flask_restful import reqparse, Resource
from .model import Tasks

json.provider.DefaultJSONProvider.ensure_ascii = False

_task_parser = reqparse.RequestParser()
_task_parser.add_argument('description',
                          type=str,
                          required=True,
                          help="This field cannot be blank"
                          )
_task_parser.add_argument('completed',
                          type=int,
                          required=True,
                          help="This field cannot be blank"
                          )
_task_parser.add_argument('ticket_id',
                          type=str,
                          required=True,
                          help="This field cannot be blank"
                          )

class GetTasks(Resource):
    def get(self):
        tasks = Tasks.query.all()
        return jsonify([task.as_dict() for task in tasks])

    def post(self):
        data = _task_parser.parse_args()
        tasks = Tasks(
            description=request.json['description'],
            completed=request.json['completed'],
            ticket_id=request.json['ticket_id'],
            )
        db.session.add(tasks)
        db.session.commit()
        return tasks.as_dict()


class Task(Resource):
    def get(self, id):
        tasks = Tasks.query.get(id)
        if tasks:
            return tasks.as_dict()
        else:
            return {'error': 'Task not found'}

    def delete(self, id):
        tasks = Tasks.query.get(id)
        if tasks:
            db.session.delete(tasks)
            db.session.commit()
            return {'data': 'Task deleted successfully'}
        else:
            return {'error': 'Task not found'}
