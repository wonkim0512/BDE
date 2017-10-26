from pymongo import MongoClient


def get_score(db):
    with open('grade.txt', 'r') as f:
        num_of_students = f.readline()
        #print(num_of_students, end="")

        line_idx = 0
        for line in f.readlines():
            edited_line = list(map(lambda x: int(x), line.rstrip().split(" ")))
            score = calculation(edited_line)
            write_score(db, line_idx, score)
            line_idx += 1



def calculation(line):
    point = 1
    score = 0
    for idx, num in enumerate(line):
        if idx == 0:
            if num == 1:
                score += point

            else:
                pass

        else:
            if line[idx-1] == 1:
                if num == 1:
                    point += 1
                    score += point

            else:
                if num == 1:
                    point = 1
                    score += point

    return score



def write_score(db, sid, score):
    db.grade.insert_one({'sid':sid, 'score': score})


def extra_point():
    db.grade.update_many({"score":55}, {"$inc":{'score': 5}}) # every matching elements
    db.grade.update({"sid":5}, {"$inc":{'score': -1}})


if __name__ == "__main__":
    client = MongoClient()
    db = client.lab2

    get_score(db)
    extra_point()
