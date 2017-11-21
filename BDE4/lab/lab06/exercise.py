import pymongo
from pymongo import MongoClient, GEOSPHERE
from pprint import pprint

def distance(x, y):
    import math
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def ex2(db):
    california_doc = db.states.find_one({'name':'California'})
    # print(california_doc['loc']['type'], california_doc['loc']['coordinates'])
    calif_airports = db.airports.find({'loc.coordinates':{'$geoWithin':{"$geometry": {'type': california_doc['loc']['type'], \
                                                  'coordinates': california_doc['loc']['coordinates']}}}}, {'_id':0, 'name':1, 'type':1, 'code':1}).sort('name', pymongo.ASCENDING)

    for airport in calif_airports:
        print(airport)

    print("*" * 80)

    SFO_coordinate = db.airports.find_one({'code':"SFO"})['loc']['coordinates']
    calif_airports = db.airports.find({'loc.coordinates': {'$geoWithin': {"$geometry": {'type': california_doc['loc']['type'], \
                                                          'coordinates': california_doc['loc']['coordinates']}}}},\
                                      {'_id': 0, 'name': 1, 'type': 1, 'code': 1, 'loc.coordinates':1})


    distances = []
    for airport in calif_airports:
        distances.append((airport['code'],distance(SFO_coordinate, airport['loc']['coordinates'])))

    print(sorted(distances, key = lambda x:x[1])[-2])


def ex3(db):
    calif = db.states.find_one({'name':'California'})
    calif_type, calif_coord = calif['loc']['type'], calif['loc']['coordinates']

    intersecting_states = db.states.find({'loc':{'$geoIntersects':{'$geometry': {'type': calif_type, 'coordinates':calif_coord}}}})

    for state in intersecting_states:
        if not state['code'] == "CA":
            print(state)

def ex4(db):
    The_reservoir_coord = [-73.965355, 40.782865]
    near_reservoirs = db.airports.find({'type': 'International', \
                                        'loc': {"$near": {"$geometry": {'type':'Point', \
                                                                        'coordinates':The_reservoir_coord},"$maxDistance": 20000}}}, {"_id":0, 'name':1})
    for reservoir in near_reservoirs:
        print(reservoir)


def ex5(db):
    pass



if __name__ == "__main__":
    db = MongoClient().lab6

    db.airports.create_index([('loc', GEOSPHERE)])
    # pprint(db.airports.index_information())
    #
    # db.airports.drop_index([('loc', GEOSPHERE)])
    # pprint(db.airports.index_information())
    #
    # db.airports.create_index([('loc', GEOSPHERE)])

    ex4(db)