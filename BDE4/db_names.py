from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db_list = client.database_names()
    print(db_list)

    db = client.test_database
    print(db)


if __name__ == "__main__":
    main()