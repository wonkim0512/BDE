# exercise 2

import pymongo
from pymongo import MongoClient
from pprint import pprint

if __name__ == "__main__":
    client = MongoClient()
    db = client.lab5
    pokedex = db.pokedex

    # 2-1
    stats = pokedex.find({'name':'Wartortle'}).explain()['executionStats']
    pprint(stats)

    # 2-2
    pokedex.create_index('name')

    # 2-3
    stats = pokedex.find({'name':'Wartortle'}).explain()['executionStats']
    pprint(stats)

    # 2-4
    pokedex.create_index([
        ('id', pymongo.DESCENDING),
        ('name', pymongo.ASCENDING) ])

    # 2-5
    pokedex.drop_indexes()
