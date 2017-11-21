from pymongo import MongoClient
import sys

def showgroup(col, number):
	cursor = col.find().sort("sid",1).skip((int(number)-1)*3).limit(3)

	for i in cursor:
		print(i)


if __name__ == "__main__":
	client = MongoClient()
	db = client.lab4
	col = db.grade

	showgroup(col, sys.argv[1])
	client.close()	
