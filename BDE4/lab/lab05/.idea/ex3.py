# exercise 3

import sys
from pymongo import MongoClient
from pprint import pprint

if __name__ == "__main__":
    client = MongoClient()
    db = client.lab5
    pokedex = db.pokedex

    wind_pokemon = []
    wind_weak = []

    # get Baram's pokemons
    for i in range(1,len(sys.argv)):
        wind_pokemon.append(sys.argv[i])

    # weaknesses of Baram's pokemons
    for w in wind_pokemon:
        wind_weak.append(pokedex.find_one({'name':w})['weaknesses'])

    # intersection of weaknesses
    weak_type = set(wind_weak[0])
    for w in wind_weak[1:]:
        weak_type = weak_type & set(w)

    weak_type = list(weak_type)

    for candidate in pokedex.find(
        {'type' : {'$in' : weak_type}},
        {'_id':0, 'id':1, 'name':1, 'type':1}).sort('name'):

        pprint(candidate)