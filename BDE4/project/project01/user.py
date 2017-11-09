# user.py
from post import *

def signup(db):

    while True:

        id = input("id: ") # id
        if not db.users.find_one({"id": id}): # if this id is not in users collection,

            while True:

                pw = input("pw: ") # password
                if not re.match('^(?=.*?\d)(?=.*?[a-zA-Z])(?=.*?[!@#$%^&*()_+=-`~])[!@#$%^&*()_+=-`~A-Za-z\d]{8,}$', pw): # password restriction
                    print("Minimum 8 characters with at least one letter, one number and one special character.")
                    continue
                break

            name = input("name: ") # name
            birthday = input("birthday(YYMMDD)") # birthday
            if '-' in birthday:
                birthday = "".join(birthday.split('-')) # get rid of '-' from user's input

            phone = input("phone number: ") # phone number
            if '-' in phone:
                phone = "".join(phone.split('-')) # get rid of '-' from user's input

            print(id, pw, name, birthday, phone,"\n")
            db.users.insert_one({"id": id, "pw": pw, "name": name, "birthday": birthday,\
                                 "phone":phone, "following":[], "followers":[]})

            return False

        print("The ID already exists. Please try another ID!\n")


def signin(db):

    while True:

        print("\nPlease Login!")
        id = input("Please input your ID: ")
        pw = input("Please input your password:")

        if not db.users.find_one({"id":id}):
            print("There is no ID like this.\n")

        else:
            if not db.users.find_one({"pw":pw}):
                print("Wrong Password!\n")

            print("Login success!\n")
            document = db.users.find_one({"id":id, "pw":pw})
            userpage(db, id, document)


def userpage(db, id, document):
    x = PrettyTable()
    x.field_names = ["no", "function"]
    x.add_row(["1", "Change my status message"])
    x.add_row(["2", "Check my following and follower list"])
    x.add_row(["3", "My posting"])
    x.add_row(["4", "Another"])

    switcher = {1: changeStatus,
                2: followList,
                3: posting} # more to do.

    while True:
        print("\nWelcome to", id + "'s userpage!")
        print(x)

        task_no = input("What do you want to do here? Please enter the task's number: \n")
        selected_task = switcher.get(int(task_no), print_wrong)
        selected_task(db, id, document)


def changeStatus(db,id,document):

    curr_status = db.status.find_one({'id':id})

    if curr_status:
        print("'{}' is your current status.".format(curr_status['status']))

        confirm = input("Are you sure to change your status?(y/n):")
        if confirm in ["Y", "y", "yes", "Yes", "YES"]:
            new_status = input("Enter new status: ")
            db.status.insert_one({'user_id': id, 'status': new_status})

        elif confirm in ["N", "n", "no", "NO", "No"]:
            pass

        else:
            print("Wrong input!")

    else:
        print("You have no status message now!")


def followList(db, id, document):

    followings = document["following"]
    followers = document["followers"]
    print(id + " has", len(followings), "followings,", len(followers), "followers")

    want_to_see_list = input("\nDo you want to see people's list?(y/n):")
    if want_to_see_list in ["Y","y","yes","Yes","YES"]:
        print("followings:", followings,"\nfollowers:", followers)


