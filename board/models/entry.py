# -*- coding: utf-8 -*-

from board import db

class Entry(db.Model):
    __tablename__ = 't_entry'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('t_user.id'), nullable=False)
    #updateed_date = db.Column(db.DateTime,  onupdate=db.func.current_timestamp())

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return '<Entry %r>' % self.id

    def getAllOrderByDate(self):
        return self.query.order_by(db.desc('created_date')).all()

    def save(self):
        db.session.add(self)
        db.session.commit()
