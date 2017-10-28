#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def delete_special_characters(book_list):
    book = []

    for works in book_list:
        work = works.replace('\n', ' ')
        work = work.replace('\r', ' ')
        work = work.replace(',', '')
        work = work.replace('.', '')
        work = work.replace(';', '')
        work = work.replace('-', '')
        work = work.replace('_', '')
        work = work.replace("''", '')

        book.append(work.lower())

    return book


def process_book(book_path):
    with codecs.open(book_path, "r", encoding='utf-8', errors='ignore') as data:
        content = data.read()

    book_list = content.split(" ")

    return delete_special_characters(book_list)