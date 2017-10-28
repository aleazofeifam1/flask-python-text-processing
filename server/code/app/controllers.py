#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import codecs, os

from app.middlewares import formato
from config import config
from db import *

class File(Resource):
    def post(self): #Save .txt file, and process la list.
        book = request.files["file"]

        book.save(os.path.join(config.FILE_FOLDER, book.filename))
        location = "{}/{}".format(config.FILE_FOLDER, book.filename)

        book = formato.process_book(location)

        return {"message": "todo sirve"}


class Print(Resource):
    def get(self, path): #Print the .txt file if it exists.
        location = "{}/{}".format(config.FILE_FOLDER, path)

        try:
            with codecs.open(location, "r", encoding="utf-8", errors='ignore') as data:
                content = data.read()
    
            return {"message": "El archivo {} existe".format(path)}
        except (OSError, IOError) as identifier:   

            return {"mesage": "El archivo {} no existe".format(path)}
