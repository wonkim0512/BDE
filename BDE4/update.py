from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.lab2
    collection = db.pypeople
    collection.update({"name": "Lee"},\
                          {'$set': {'name': "Lim", 'age': 25}})

    collection.update({'name': 'Kim'}, {"$set": {'age': 20}})
    collection.update({'name': "Park"}, {"$unset": {'skills': ""}})
    collection.update({'name': 'Choi'}, {"$inc": {'score':-2}})

    for result in db.pypeople.find():
        print(result)

    client.close()

if __name__ == "__main__":
    main()