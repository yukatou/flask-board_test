# -*- coding: utf-8 -*-

from board import db

class User(db.Model):
    __tablename__ = 't_user'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False, unique=True)
    created_date = db.Column(db.DateTime, default=db.func.now())
    entry = db.relationship('Entry', backref='user', lazy='join')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()

    def getByUsername(self, username=None):
        return self.query.filter_by(username=username).first()

