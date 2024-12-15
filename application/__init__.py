from flask import Flask
from flask_restful import Api
from .db import init_db
from .app import Task, GetTasks


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    init_db(app)

    api.add_resource(GetTasks, '/api/tasks')
    api.add_resource(Task, '/api/task/<int:id>')

    return app
