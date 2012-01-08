#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
from board.conf import Development

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)

from board.controllers.board_controller import board
app.register_module(board, url_prefix='/board')


@app.route("/db/create")
def create_all():
    db.create_all()
    return 'DB tables created'

@app.route("/db/drop")
def drop_all():
    db.drop_all()
    return 'DB tables dropped'
