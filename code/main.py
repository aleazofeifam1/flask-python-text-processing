#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re
from flask import Flask, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import codecs

app = Flask(__name__)
api = Api(app)

client = MongoClient('192.168.12.169', 27017)
db = client.repository

verbs_collection = db.verbs
adjetivos_collection = db.adjetivos
sinominos_collection = db.sinominos

folder = "/tmp"

def format_book(book_path):

    with codecs.open(book_path, "r",encoding='utf-8', errors='ignore') as f:
        content = f.read()

    print(type(content))
    data = content.split(" ")


    final = []
    for works in data:
        work = works.replace('\n', ' ')
        work = work.replace('\r', ' ')
        #work = work.replace(' ', '')
        work = work.replace(',', '')
        work = work.replace('.', '')
        work = work.replace(';', '')
        work = work.replace('-', '')
        work = work.replace('_', '')
        #work = work.replace('?', '')
        #work = work.replace('!', '')
        work = work.replace("''", '')
        final.append(work.lower())
    
    print(final)
    return final



class Save(Resource):
    def post(self):
        book = request.files["file"]
        book.save(os.path.join(folder, book.filename))

        location = "{}/{}".format(folder, book.filename)
        book = format_book(location)

        verbos      = verbs_collection.find({"work" : {"$in" : book}}).count()
        sinominos   = sinominos_collection.find({"work" : {"$in" : book}}).count()
        adjetivos   = adjetivos_collection.find({"work" : {"$in" : book}}).count()
        return {"message": "Verbos:{}, Sinonimos:{}, Adjetivos{}".format(verbos, sinominos, adjetivos)}, 201


class Print(Resource):
    def get(self, path):
        location = "{}/{}".format(folder, path)

        try:
            archivo = open(location,"r")
            contenido = archivo.read()

            return {"mesage": contenido}
        except (OSError, IOError) as identifier:

            return {"mesage": "archivo no existe"}

api.add_resource(Save, '/uploader')
api.add_resource(Print, '/files/<string:path>')


if __name__ == '__main__':
    app.run(debug=True)
