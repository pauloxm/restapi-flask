from flask import Flask
from flask_restful import Api
from .db import init_db
from .app import Default, Login, GetTasks, HealthChecks, Task


def create_app(DevConfig):
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    api = Api(app)
    init_db(app)

    api.add_resource(Default, '/')
    api.add_resource(Login, '/login')
    api.add_resource(GetTasks, '/api/tasks')
    api.add_resource(HealthChecks, '/health')
    api.add_resource(Task, '/api/task/<int:id>')

    return app
