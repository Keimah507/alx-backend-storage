#!/usr/bin/ env python3
"""Lists all documents in a collection"""
import pymongo
import pprint


def list_all(mongo_collection):
    """Lists all documents in mongo_collection"""
    for doc in mongo_collection.find():
        pprint.pprint(doc)
