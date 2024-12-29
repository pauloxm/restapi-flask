from flask import Flask
from flask_restful import Api
from .db import init_db
from .app import Default, Login, GetTasks, HealthChecks, Task
from prometheus_flask_exporter import PrometheusMetrics


def create_app(DevConfig):
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    # Initialize Prometheus metrics
    PrometheusMetrics(app)

    init_db(app)

    api = Api(app)

    api.add_resource(Default, '/')
    api.add_resource(Login, '/login')
    api.add_resource(GetTasks, '/api/tasks')
    api.add_resource(HealthChecks, '/health')
    api.add_resource(Task, '/api/task/<int:id>')

    return app

def create_app(ProdConfig):
    app = Flask(__name__)
    app.config.from_object(ProdConfig)

    # Initialize Prometheus metrics
    PrometheusMetrics(app)

    init_db(app)

    api = Api(app)

    api.add_resource(Default, '/')
    api.add_resource(Login, '/login')
    api.add_resource(GetTasks, '/api/tasks')
    api.add_resource(HealthChecks, '/health')
    api.add_resource(Task, '/api/task/<int:id>')

    return app
