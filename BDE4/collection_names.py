from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client.lab2
    collection_list = db.collection_names()
    print(collection_list)




if __name__ == "__main__":
    main()