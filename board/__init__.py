#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flaskext.sqlalchemy import SQLAlchemy
from board.conf import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
#app.config.from_object(ProductionConfig)
db = SQLAlchemy(app)

from board.controllers.board_controller import app as board
app.register_blueprint(board, url_prefix='/board')


@app.route("/db/create")
def create_all():
    db.create_all()
    return 'DB tables created'

@app.route("/db/drop")
def drop_all():
    db.drop_all()
    return 'DB tables dropped'

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error=e), 500
