#!/usr/bin/env python3
"""Changes all the topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Changes all the topics of mongo_collection based on the name"""
    result = mongo_collection.update_many({name: topics}, {'$inc': {name: topics}})
