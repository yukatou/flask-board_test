#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import site

activate_this = '/home/yukatou/.virtualenvs/board_test/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# Flaskアプリケーショントップのパスをpathに追加
sys.path.append('/home/yukatou/workspace/python/board_test') 

#def application(environ, start_response):
#    status = '200 OK'
#    #output = 'Hello World!'
#    output = '\n'.join(sys.path)

#    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
#    return [output]

from board import app as application
