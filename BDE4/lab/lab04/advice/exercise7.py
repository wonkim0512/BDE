from pymongo import MongoClient
import sys

def letter(score):
	if score>= 90:
		return "A"
	elif score>=80:
		return "B"
	elif score>=70:
		return "C"
	elif score>=60:
		return "D"
	else:
		return "F"


def grading(col):

	sum = 0
	for k in range(0, 100):
		cursor = col.find().sort("sid",1).skip(k*3).limit(3)
		quiz = 0
		homework = 0
		exam = 0
		for i in cursor:
			if i["type"] == "quiz":
				quiz = i["score"]
			elif i["type"] == "homework":
				homework = i["score"]
			else:
				exam = i["score"]
		total = quiz * 0.2 + homework * 0.3 + exam * 0.5
		sum = sum + total
		db.letter.insert_one({"sid": i["sid"], "letter": letter(total)})
	print("average: ", sum/100)

if __name__ == "__main__":
	client = MongoClient()
	db = client.lab4
	col = db.grade
	grading(col)
	client.close()	
