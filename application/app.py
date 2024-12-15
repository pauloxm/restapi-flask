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


# Metodo de representação
def __repr__(self):
    return f"Tasks('{self.description}','{self.completed}')"


# Monta o dicionario para serialização
def as_dict(self):
    return {c.description: getattr(self, c.description)
            for c in self.__table__.columns}


class GetTasks(Resource):
    def get(self):
        tasks = GetTasks.query.all()
        return jsonify([task.as_dict() for task in tasks])

    def post(self):
        new_task = Tasks(
            description=request.json['description'],
            completed=request.json['completed'],
            )
        db.session.add(new_task)
        db.session.commit()
        return new_task.as_dict()


class Task(Resource):
    def get(self, id):
        task = Tasks.query.get(id)
        if task:
            return task.as_dict()
        else:
            return {'error': 'Task not found'}

    def delete(self, id):
        task = Tasks.query.get(id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'data': 'Task deleted successfully'}
        else:
            return {'error': 'Task not found'}
