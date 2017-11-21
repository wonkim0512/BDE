from pymongo import MongoClient
import sys

def ex4(db):
    try:
        db.sales.insert_one({"_id": 4, "item":{"category":"Camera", "type": "Digital"}, "amount":15})

    except Exception as e:
        print(e)

def ex5(db):
    for sid in range(100):
        if db.grade.find({'sid':sid}).count() != 3:
            #db.grade.insert_one({'sid':sid, 'type':'quiz', 'score':80})
            print(sid)

def ex6(db):
    number = int(input('number:')) #input() is string.
    cursor = db.grade.find().sort("sid", 1).skip((int(number)-1)*3).limit(3)
    for doc in cursor:
        print(doc)

def ex7(db):
    quiz, homework, exam = {}, {}, {}


    for sid in range(100):
        cursor = db.grade.find({'sid':sid})
        for doc in cursor:
            if doc['type'] == 'quiz':
                quiz[sid] = doc['score']

            elif doc['type'] == 'homework':
                homework[sid] = doc['score']

            else:
                exam[sid] = doc['score']

    for sid in range(100):
        total = quiz[sid]*0.2 + homework[sid]*0.3 + exam[sid]*0.5

        if total >= 90:
            db.letter.insert_one({'sid':sid, "letter": "A"})

        elif total >= 80:
            db.letter.insert_one({'sid': sid, "letter": "B"})

        elif total >= 70:
            db.letter.insert_one({'sid': sid, "letter": "C"})

        elif total >= 60:
            db.letter.insert_one({'sid': sid, "letter": "D"})

        else:
            db.letter.insert_one({'sid': sid, 'letter': "F"})


if __name__ == "__main__":
    client = MongoClient()
    db = client.lab4

    ex4(db)
    ex5(db)
    ex6(db) #, sys.argv[1])
    ex7(db)

    client.close()