from pymongo import MongoClient

def miss(col):
	
	for i in range(0, 100):
		cursor = col.find({"sid": i})
		if cursor.count() != 3:
			col.insert_one({"sid": i, "type": "quiz", "score": 80})
			print(i)
			break


if __name__ == "__main__":
	client = MongoClient()
	db = client.lab4
	col = db.grade

	miss(col)
	client.close()	
