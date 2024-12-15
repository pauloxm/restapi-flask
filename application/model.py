from .db import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Integer, nullable=False)
