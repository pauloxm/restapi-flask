from .db import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Integer, nullable=False)
    ticket_id = db.Column(db.String(11), nullable=False)

    # Metodo de representação
    def __repr__(self):
        return f"Tasks('{self.description}','{self.completed}','{self.ticket_id}')"

    # Monta o dicionario para serialização
    def as_dict(self):
        return {c.description: getattr(self, c.description)
                for c in self.__table__.columns}
