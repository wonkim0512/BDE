from pymongo import MongoClient, errors

client = MongoClient()
db = client.lab4

# exercise 4
try:
    db.sales.insert_one({"_id": 4, "item": { "category": "Camera", "type": "Digital" }, "amount": 15 })


except Exception as e:
    print(e)



# exercise 5

for sid in range(100):
    if db.grade.find({"sid":sid}).count() != 3:
        db.grade.insert_one({'sid': sid, 'type': 'quiz',\
                                    'score': 80})
        break


# exercise 6

def showgroup(number):
   pass


# exercise 7


def calculate(sid):

    result = db.grade.find({'sid': sid})

    for i in result:
        if i["type"] == 'quiz':
            quiz_score = i['score']

        elif i['type'] == 'exam':
            exam_score = i['score']

        else:
            hw_score = i['score']


    total = quiz_score*0.2 + hw_score*0.3 + exam_score*0.5

    if total >= 90:
        return sid, "A"

    elif total >= 80:
        return sid, "B"

    elif total >= 70:
        return sid, "C"

    elif total >= 60:
        return sid, "D"

    else:
        return sid, "F"

def grading():

    db.letter.drop()

    for sid in range(100):
        sid, grade = calculate(sid)
        db.letter.insert_one({'sid':sid, 'grade':grade})

grading()