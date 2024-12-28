from flask import request, jsonify, json
from .db import db
from flask_restful import reqparse, Resource
from .model import Tasks, Healthcheck
from sqlalchemy import exc
import jwt
import os
from datetime import datetime, timedelta, timezone


json.provider.DefaultJSONProvider.ensure_ascii = False

SECRET_KEY = os.getenv("SECRET_KEY")

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


class Default(Resource):
    def get(self):
        return {"message": "Welcome to the secure API with JWT"}


class HealthChecks(Resource):
    def get(self):
        try:
            healthcheck = Healthcheck.query.first()
            if healthcheck:
                return {"Healthcheck": "OK"}, 200
            else:
                new_healthcheck = Healthcheck(status=1)
                db.session.add(new_healthcheck)
                db.session.commit()
                db.session.refresh(new_healthcheck)
                return {"Healthcheck": "OK"}, 200
        except Exception:
            return {"Healthcheck": "NOK"}, 400


class Login(Resource):
    def get(self):
        data = request.get_json()
        if not data:
            return {"message": "Login data is missing"}, 400
        if "username" not in data or "password" not in data:
            return {"message": "Fields 'username' and "
                    "'password' are mandatory"}, 400
        if data["username"] == "admin" and data["password"] == "123":
            # Gerar o token com expiração
            token = jwt.encode(
                {"user": data["username"],
                 "exp": datetime.now(timezone.utc) + timedelta(minutes=30)},
                SECRET_KEY,
                algorithm="HS256"
            )
            return jsonify(token=token)

        return {"message": "Invalid login"}, 401


class GetTasks(Resource):
    def get(self):
        tasks = Tasks.query.all()
        return jsonify([task.as_dict() for task in tasks])

    def post(self):
        tasks = Tasks(
            description=request.json['description'],
            completed=request.json['completed'],
            ticket_id=request.json['ticket_id'],
            )
        try:
            db.session.add(tasks)
            db.session.commit()
            return tasks.as_dict()
        except exc.IntegrityError:
            return {"message": "Ticket ID already exists"}, 400


class Task(Resource):
    def get(self, id):
        # Obtém o token do cabeçalho da requisição
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return {"message": "Absent Token"}, 403

        parts = auth_header.split()
        if parts[0].lower() != 'bearer' or len(parts) != 2:
            return {"message": "Malformed Authorization header"}, 401
        token = parts[1]

        try:
            # Decodifica o token
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            tasks = Tasks.query.get(id)
            if tasks:
                return tasks.as_dict()
            else:
                return {"error": "Task not found"}
        except jwt.ExpiredSignatureError:
            return {"message": "Expired Token"}, 401
        except jwt.InvalidTokenError:
            return {"message": "Invalid Token"}, 403

    def delete(self, id):
        # Obtém o token do cabeçalho da requisição
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return {"message": "Absent Token"}, 403

        parts = auth_header.split()
        if parts[0].lower() != 'bearer' or len(parts) != 2:
            return {"message": "Malformed Authorization header"}, 401
        token = parts[1]

        try:
            # Decodifica o token
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            tasks = Tasks.query.get(id)
            if tasks:
                db.session.delete(tasks)
                db.session.commit()
                return {'data': 'Task deleted successfully'}, 200
            else:
                return {'error': 'Task not found'}
        except jwt.ExpiredSignatureError:
            return {"message": "Expired Token"}, 401
        except jwt.InvalidTokenError:
            return {"message": "Invalid Token"}, 403
