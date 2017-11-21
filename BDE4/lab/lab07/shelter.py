import pymongo
from pprint import pprint
from bson.son import SON


def ex1(db):
    db.shelter.drop_indexes()
    db.shelter.create_index([('province',pymongo.TEXT),\
                             ('city', pymongo.TEXT)])
    pprint(db.shelter.index_information())


def ex2(db):
    db.shelter.drop_indexes() # collection에 text index는 1개.
    db.shelter.create_index([('province', pymongo.TEXT)])
    Kangwon_1000 = db.shelter.find({'province': '강원도', 'occupancy':{"$gte":1000}},\
            {'_id':0, 'province':1, 'name':1, 'occupancy':1}).sort('occupancy', pymongo.ASCENDING)

    for i in Kangwon_1000:
        print(i)


def ex3(db):
    db.shelter.drop_indexes()  # collection에 text index는 1개.
    db.shelter.create_index([('province', pymongo.TEXT)])
    pusan_1000_6000 = db.shelter.aggregate([
        {"$match": {'$text': {'$search': '부산광역시'}}},
        {"$match": {'occupancy':{"$gte":1000, "$lte":6000}}},
        {'$project':{'_id':0, "name":1, "address":1, "location":1}},
        {'$sort': SON([('name', pymongo.ASCENDING)])}
    ])
    for i in pusan_1000_6000:
        print(i)


def ex4(db):
    db.shelter.drop_indexes()  # collection에 text index는 1개.
    db.shelter.create_index([('province', pymongo.TEXT)])
    pipeline = [
        {'$group':{'_id': {'province': "$province"}, 'count':{"$sum":1}, 'avg_occupancy':{"$avg":"$occupancy"}}},
        {'$project': {'_id':0, 'province':1, 'name':1, "count":1, "avg_occupancy":1}}
    ]
    province_info = db.shelter.aggregate(pipeline)
    for i in province_info:
        print(i)


def ex5(db):
    db.shelter.drop_indexes()
    db.shelter.create_index([('location', pymongo.GEOSPHERE)])

    pipeline = [
        {'$geoNear':{
            'near':{'type': 'Point', 'coordinates':[129.630170, 35.689834]},
            'distanceField': 'Distance',
            'maxDistance': 20000,
            'spherical': True}
        },

        {'$group': {
            '_id':{'province': "$province"},
            'count': {"$sum":1},
            'total_occupancy': {"$sum": "$occupancy"},
            'avg_distancefromsea': {"$avg": "$distancefromsea"}}
        }
   ]

    tsunami_shelter = db.shelter.aggregate(pipeline)
    for i in tsunami_shelter:
        print(i)



if __name__ == "__main__":
    client = pymongo.MongoClient()
    db = client.lab7

    # ex1(db)
    # ex2(db)
    # ex3(db)
    # ex4(db)
    ex5(db)