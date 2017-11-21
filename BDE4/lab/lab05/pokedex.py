import sys
from pymongo import MongoClient
import re
from pprint import pprint

client = MongoClient()
db = client.lab5

def displayStats(name = "Wartortle"):
    #name = input("Which character do you want to see?: ")
    executionStats = db.pokedex.find({"name": name}).explain()["executionStats"]
    pprint(executionStats)


def weakness(*args):
    args = sys.argv
    weaknesses = {}
    for arg in args[1:]:
        weakness = db.pokedex.find_one({"name": arg})['weaknesses']

        for i in weakness:
            if not i in weaknesses:
                weaknesses[i] = 1

            else:
                weaknesses[i] += 1

    commons = []
    for i in weaknesses:
        if weaknesses[i] == len(args)-1:
            commons.append(i)

    rivals = db.pokedex.find({'weaknesses':{"$in":commons}}, {"_id":True, "name":True, "type":True}).sort("name", 1)
    for rival in rivals:
        pprint(rival)

def pokemonHunting():
    appears = db.pokedex.find({"spawn_time":{"$in":[re.compile("^20:"),re.compile("^21:"),\
                                                   re.compile("^22:"),re.compile("^23:"),re.compile("^24:")]}}, \
                              {"_id": False, "id":True, "name": True, "spawn_time": True})

    for appear in appears:
        print(appear)

if __name__ == "__main__":
    displayStats()
    weakness()
    pokemonHunting()
