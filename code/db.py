#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from config import config

connection = MongoClient(config.DB_HOST, config.DB_PORT)
database = connection.repository

verbs_collection = database.verbs
adjetivos_collection = database.adjectives
sinominos_collection = database.synonyms
pronouns_collection = database.pronouns
nouns_collection = database.nouns




def find_verbs(book):
    return verbs_collection.find({"work" : {"$in" : book}}).count()

def find_adjetives(book):
    return adjetivos_collection.find({"work" : {"$in" : book}}).count()

def find_sinonimos(book):
    return sinominos_collection.find({"work" : {"$in" : book}}).count()

def find_pronombres(book):
    return pronouns_collection.find({"work" : {"$in" : book}}).count()

def find_nouns(book):
    return nouns_collection.find({"work" : {"$in" : book}}).count()

