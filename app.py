from flask import Flask
# Importa as bibliotecas Resource e API
from flask_restful import Resource, Api

app = Flask(__name__)
# Comando abaixo cria API com flask Restful
api = Api(app)


# Criar uma classe cujo nome começa com uma letra maiuscula.
# Nome da classe baseado na entidade que será atendida
# Ex.: Usuario/Users, etc.
class HelloWorld(Resource):
    # Define o método a ser utilizado. GET ou POST
    def get(self):
        # Retona o JSON
        return {'hello': 'world'}


class Users(Resource):
    def get(self):
        return {'message': 'user 1'}


class User(Resource):
    def get(self):
        return {'message': 'CPF'}

    def post(self):
        return {'message': 'teste'}


# Cria um recursos adicionando uma rota para o endpoint
# api.add_resource(HelloWorld, '/')
api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

# Define que a variavel __name__ será igual a __main__,
# dessa forma permite executar direto com o comando python3 app.py
if __name__ == '__main__':
    # Executa no modo Debug e define que vai escutar em todas as interfaces
    app.run(debug=True, host="0.0.0.0")
