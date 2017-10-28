#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from app.controllers import *

app = Flask(__name__)
api = Api(app)

api.add_resource(File, '/uploader')
api.add_resource(Print, '/files/<string:path>')


if __name__ == '__main__':
    app.run(debug=True)