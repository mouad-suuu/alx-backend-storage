#!/usr/bin/env python3
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    :param mongo_collection: pymongo collection object
    :param kwargs: keyword arguments that define the document to insert
    :return: the new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
