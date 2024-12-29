from .db import db
from werkzeug.security import generate_password_hash, check_password_hash


class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Integer, nullable=False)
    ticket_id = db.Column(db.String(11), nullable=False)

    # Metodo de representação
    def __repr__(self):
        return (
            "Tasks('{self.description}',"
            "'{self.completed}',"
            "'{self.ticket_id}')"
        )

    # Monta o dicionario para serialização
    def as_dict(self):
        return {c.description: getattr(self, c.description)
                for c in self.__table__.columns}


class Healthcheck(db.Model):
    __tablename__ = 'healthcheck'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(1), nullable=False)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=True)

    # Check password
    def check_password(self, password):
        # Criar o hash da senha passada no campo password para
        # fazer validação com o que vem do banco
        hashed_password = generate_password_hash(password)
        return check_password_hash(hashed_password, self.password)

    # Set password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
