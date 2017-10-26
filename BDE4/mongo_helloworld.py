from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.lab2
    db.posts.insert_one({"Author": "Won Kim",\
                         "Text": "Hello World!"})
    print(db.posts.find_one())


if __name__ == "__main__":
    main()