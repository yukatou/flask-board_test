# -*- coding: utf-8 -*-

from werkzeug import generate_password_hash, check_password_hash
from board import db

class User(db.Model):
    __tablename__ = 't_user'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False, unique=True)
    created_date = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

