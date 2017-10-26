# user.py
import re
from prettytable import PrettyTable

def signup(db):

    while True:

        id = input("id: ") # id

        if not db.users.find_one({"id": id}): # if this id is not in users collection,
            pw = input("pw: ") # password

            if not re.match('^(?=.*?\d)(?=.*?[a-zA-Z])(?=.*?[!@#$%^&*()_+=-`~])[!@#$%^&*()_+=-`~A-Za-z\d]{8,}$', pw): # password restriction
                print("Minimum 8 characters with at least one letter, one number and one special character.")
                continue

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


    '''
    1. Get his/her information.
    2. Check if his/her password equals confirm password.
    3. Check if the userid already exists.
    4. Make the user document.
    5. Insert the document into users collection.
    '''


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
            userpage(db, id)


    '''
    1. Get his/her information.
    2. Find him/her in users collection.
    3. If exists, print welcome message and call userpage()
    '''


def followList(db, user, document):
    followings = document["following"]
    followers = document["followers"]
    print(user + " has", len(followings), "followings,", len(followers), "followers")

    want_to_see_list = eval("Do you want to see people's list?(y/n):")
    if want_to_see_list in ["Y","y","yes","Yes","YES"]:
        print("followings:", followings,"\nfollowers:", followers)


def userpage(db, user):
    x = PrettyTable()
    x.field_names = ["no", "function"]
    x.add_row(["1", "Change my status messege"])
    x.add_row(["2", "Check my following and follower list"])
    x.add_row(["3", "Another"])
    x.add_row(["4", "Another"])

    switcher = {2: followList} # more to do.

    print("Welcome to", user + "'s userpage!")
    print(x)

    task_no = input("What do you want to do here? Please enter the task's number: ")
    selected_task = switcher.get(int(task_no), print_wrong)
    selected_task() # parameter 넘겨줘야하는 경우에는 어떡하지???



def print_wrong():
    print("\nwrong menu number.")
