#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pymongo import MongoClient

db_host = "192.168.0.106"
db_port = 27017

# Database: repository
# Collections: verbs, adjectives, synonyms, pronouns, nouns
# format ====> {"work" : "@data"}

connection = MongoClient(db_host, db_port)
database = connection.repository

def delete_special_characters(data_list):
    final_list = []

    for works in data_list:
        work = works.replace('\n', ' ')
        work = work.replace('\r', ' ')
        work = work.replace(',', '')
        work = work.replace(' ', '')
        work = work.replace('.', '')
        work = work.replace(';', '')
        work = work.replace('-', '')
        work = work.replace('_', '')
        work = work.replace("''", '')

        final_list.append(work.lower())

    return final_list


def save_verbs():
    verbs_file = open("txt_files/verbs.txt", "r")

    verbs_list = []
    for line in verbs_file.readlines():
        verbs_list.append(line)

    formatted_verbs = delete_special_characters(verbs_list)

    for data in formatted_verbs:
        mongo_data = {"work": data}
        database.verbs.insert_one(mongo_data).inserted_id
        print(mongo_data)


def save_pronouns():
    pronouns_file = open("txt_files/pronouns.txt", "r")

    pronouns_list = []
    for line in pronouns_file.readlines():
        pronouns_list.append(line)

    formatted_pronouns = delete_special_characters(pronouns_list)

    for data in formatted_pronouns:
        mongo_data = {"work": data}
        database.pronouns.insert_one(mongo_data).inserted_id
        print(mongo_data)


def save_adjectives():
    adjectives_file = open("txt_files/adjectives.txt", "r")

    adjectives_list = []
    for line in adjectives_file.readlines():
        adjectives_list.append(line)

    formatted_adjectives = delete_special_characters(adjectives_list)

    for data in formatted_adjectives:
        mongo_data = {"work": data}
        database.adjectives.insert_one(mongo_data).inserted_id
        print(mongo_data)


def save_synonyms():
    synonyms_file = open("txt_files/synonyms.txt", "r")

    content = synonyms_file.read()
    synonyms_list = content.split(" ")
    synonyms_list = [d.replace("\n", '') for d in synonyms_list]
    synonyms_list = list(filter(None, synonyms_list))

    formatted_synonyms = delete_special_characters(synonyms_list)

    for data in formatted_synonyms:
        mongo_data = {"work": data}
        database.synonyms.insert_one(mongo_data).inserted_id
        print(mongo_data)



#save_adjectives()
#save_synonyms()
#save_verbs()
#save_pronouns()