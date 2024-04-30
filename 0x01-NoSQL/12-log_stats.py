#!/usr/bin/env python3
""" Nginx logs stats script """
from pymongo import MongoClient


def log_stats():
    """ Prints statistics about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count of methods
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"    method {method}: {count}")

    # Count of documents where method=GET and path=/status
    status_check = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
