#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from config import config

connection = MongoClient(config.DB_HOST, config.DB_PORT)
database = connection.repository

def verb_connection():
    return database.verbs

def adjetivos_connection():
    return database.adjetivos

def sinominos_connection():
    return database.sinominos
