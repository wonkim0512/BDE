import pymongo
from pymongo import MongoClient
from pprint import pprint
import sys


def ex2(db):
    pprint(db.pokedex.find({'name':"Wartortle"}).explain()["executionStats"])
    db.pokedex.create_index([('name', pymongo.ASCENDING)])
    for index in db.pokedex.list_indexes():
        print(index)

    pprint(db.pokedex.find({'name':"Wartortle"}).explain()['executionStats'])
    db.pokedex.create_index([('id', pymongo.DESCENDING), ('name', pymongo.ASCENDING)])
    for index in db.pokedex.list_indexes():
        print(index)

    db.pokedex.drop_indexes()


def weaknesses(db, *args):

    Baram_pokemon = sys.argv[1:]
    Baram_pokemon_weak = {}

    for pokemon in Baram_pokemon:
        weaknesses = db.pokedex.find_one({'name': pokemon})["weaknesses"]

        for weakness in weaknesses:

            if not Baram_pokemon_weak.get(weakness):
                Baram_pokemon_weak[weakness] = 1

            else:
                Baram_pokemon_weak[weakness] += 1


    rivals = db.pokedex.find({'type': {"$in": [k for k, v in Baram_pokemon_weak.items() if v == 3]}},\
                             {'_id':0, 'name':1, 'type':1}).sort([('name', pymongo.ASCENDING)])

    for rival in rivals:
        print(rival)


if __name__ == "__main__":
    client = MongoClient()
    db = client.lab5

    # ex2(db)
    weaknesses(db)