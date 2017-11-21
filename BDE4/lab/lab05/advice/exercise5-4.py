# exercise 5-4

import re
from pymongo import MongoClient
from pprint import pprint

if __name__ == "__main__":
    client = MongoClient()
    db = client.lab5
    pokedex = db.pokedex

    for cand in pokedex.find({'spawn_time': {'$in' :
        [re.compile('^20:'), re.compile('^21:'), re.compile('^22:'), re.compile('^23:')]}},
        {'_id':0, 'id':1, 'name':1, 'spawn_time':1}).sort('spawn_time'):

        pprint(cand)
