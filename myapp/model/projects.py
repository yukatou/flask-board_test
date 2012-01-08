# -*- coding: utf-8 -*-

from flaskext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Entry(db.Model):
    __tablename__ = 't_entry'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('t_user.id'), nullable=False)
    #updateed_date = db.Column(db.DateTime,  onupdate=db.func.current_timestamp())

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Entry %r>' % self.id

    def getAllOrderByDate(self):
        return self.query.order_by(db.desc('created_date')).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

class User(db.Model):
    __tablename__ = 't_user'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False, unique=True)
    created_date = db.Column(db.DateTime, default=db.func.now())
    entry = db.relationship('Entry', backref='user', lazy='dyamic')

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
