from .db import db


class Tasks(db.Model):
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
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(1), nullable=False)

    # Metodo de representação
    def __repr__(self):
        return "HealthCheck('{self.status}')"

    # Monta o dicionario para serialização
    def as_dict(self):
        return {c.status: getattr(self, c.status)
                for c in self.__table__.columns}
