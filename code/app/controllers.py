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

        libro = formato.process_book(location)

        verbos = find_verbs(libro)
        adjetivos = find_adjetives(libro)
        sinominos = find_sinonimos(libro)
        pronombres = find_pronombres(libro)
        

        return {"message": "El libro {} tiene {} verbos, {} adjetivos, {} sinonimos y {} pronombres".format(str(book.filename), verbos, adjetivos, sinominos, pronombres)}


class Print(Resource):
    def get(self, path): #Print the .txt file if it exists.
        location = "{}/{}".format(config.FILE_FOLDER, path)

        try:
            with codecs.open(location, "r", encoding="utf-8", errors='ignore') as data:
                content = data.read()
    
            return {"message": "El archivo {} existe".format(path)}
        except (OSError, IOError) as identifier:   

            return {"mesage": "El archivo {} no existe".format(path)}

        #verbos      = verbs_collection.find({"work" : {"$in" : book}}).count()
        #sinominos   = sinominos_collection.find({"work" : {"$in" : book}}).count()
        ##adjetivos   = adjetivos_collection.find({"work" : {"$in" : book}}).count()
        #return {"message": "Verbos:{}, Sinonimos:{}, Adjetivos{}".format(verbos, sinominos, adjetivos)}, 201