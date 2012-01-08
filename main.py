#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from configure import Development
from myapp.controller.projects import projects
from myapp.model.projects import db

app = Flask(__name__)
app.config.from_object(Development)
app.register_module(projects, url_prefix='/projects')
db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
