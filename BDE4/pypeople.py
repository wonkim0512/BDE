from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.lab2
    db.pypeople.drop()
    collection = db.pypeople
    collection.insert_many([{"name": "Kim","age": 21},
                            {"name": "Lee", "age": 22},
                            {"name": "Park", "age": 27, "skills":["mongodb", "python"]},
                            {"name": "Kim", "age": 22, "score":10}]
                            )
    results = collection.find()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()