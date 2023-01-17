#!/usr/bin/env python3
"""Inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in mongo_collection"""
    new_school = mongo_collection.insert_one(kwargs)
    return new_school
    