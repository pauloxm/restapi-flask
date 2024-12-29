from .db import db


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

    # Metodo de representação
    def __repr__(self):
        return "HealthCheck('{self.status}')"

    # Monta o dicionario para serialização
    def as_dict(self):
        return {c.status: getattr(self, c.status)
                for c in self.__table__.columns}


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=True)

    # Metodo de representação
    def __repr__(self):
        return (
            "Users('{self.login}',"
            "'{self.password}',"
            "'{self.name}')"
        )

    # Monta o dicionario para serialização
    def as_dict(self):
        return {c.login: getattr(self, c.login)
                for c in self.__table__.columns}
