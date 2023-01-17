#!/usr/bin/python3
"""Python script that returns the list of schools having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """Returns list of schools having a specific topic"""
    return (mongo_collection.find({"topic": topic}))