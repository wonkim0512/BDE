from pymongo import MongoClient

client = MongoClient()
db = client.lab3
collection = db.grades


def main():
    collection.drop() # prevent collection from duplication

    with open('grade.txt', 'r') as f:
        people_count = f.readline()
        print(people_count) # people count check

        for line in f.readlines():
            name, grade = grading(line)
            print(name, grade) # calculation check
            collection.insert_one({"name": name, "grade": grade})


def grading(line):
    score = line.split(" ")
    name = score[0]
    mid = int(score[1])
    final = int(score[2])

    total = (mid + final)/2

    if total >= 90:
        return name, "A"

    elif total >= 80:
        return name, "B"

    elif total >= 70:
        return name, "C"

    else:
        return name, "D"


if __name__ == "__main__":
    main()