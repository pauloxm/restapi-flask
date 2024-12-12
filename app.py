from flask import Flask, request, jsonify, json
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://root:admin@mariadb/flask'
json.provider.DefaultJSONProvider.ensure_ascii = False
db = SQLAlchemy(app)


# Classe referente a tabela do banco
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Integer, nullable=False)

    # Metodo de representação
    def __repr__(self):
        return f"Tasks('{self.description}','{self.completed}')"

    # Monta o dicionario para serialização
    def as_dict(self):
        return {c.description: getattr(self, c.description) for c in self.__table__.columns}


# Comando abaixo cria API com flask Restful
api = Api(app)


@app.route('/api/tasks', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        tasks = Tasks.query.all()
        return jsonify([task.as_dict() for task in tasks])

    if request.method == 'POST':
        tasks = Tasks.query.all()
        return jsonify([task.as_dict() for task in tasks])

@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_tasks(id):
    task = Tasks.query.get(id)
    if task:
        return task.as_dict()
    else:
        {'error':'Task not found'}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
