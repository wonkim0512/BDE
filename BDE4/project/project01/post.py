import re
from prettytable import PrettyTable
import datetime

def posting(db, id, document):
    postInterface(db, id)

def postInterface(db, id):

    x = PrettyTable()
    x.field_names = ["Post_num", "ID", "Post"]

    posts = db.posts.find({'user_id': id})
    for post in posts:
        x.add_row([post['post_num'], id, post['post']]) # post number 어떻게 가져올지 생각해보자.

    print(x)

    task = input("1: Insert post, 2: Delete post, 0: quit: ")
    if task == "1":
        insertPost(db, id)

    elif task == "2":
        deletePost(db, id)

    elif task == "0":
        exit()

    else:
        print_wrong()



    """
    Implementing the interface to post your text.
    There are three or more items to choose functions such as inserting and deleting a text.
    """

def insertPost(db, id):
    post_num = db.posts.find({'user_id': id}).count() + 1
    post = input("Write post here: ")
    dt = datetime.datetime.now()
    db.posts.insert_one({"post_num": post_num, "user_id": id, 'post': post, 'year': dt.year, 'month': dt.month,\
                        'day': dt.day, 'hour': dt.hour, 'minute': dt.minute, 'second': dt.second})

    """
    Insert user's text. You should create the post schema including,
    for example, posting date, posting id or name, and comments.
    
    You should consider how to delete the text.
    """
	

def deletePost(db, id):
    want_to_delete_post = input("Which post do you want to delete? Please enter the post number: ")
    #id_verification = input("Please enter your id again: ")
    pw_verification = input("Please enter your password again: ")
    real_pw = db.users.find_one({'id':id})['pw']

    if pw_verification == real_pw:
        confirm = input("Are you sure to delete post number{}?(y/n):".format(want_to_delete_post))

        if confirm in ["Y","y","yes","Yes","YES"]:
            db.posts.delete_one({'user_id': id, 'post_num': int(want_to_delete_post)})

        elif confirm in ["N", "n", "no", "NO", "No"]:
            pass

        else:
            print("Wrong input!")



    """
    Delete user's text.
    With the post schema, you can remove posts by some conditions that you specify.
    """

    """
    Sometimes, users make a mistake to insert or delete their text.
    We recommend that you write the double-checking code to avoid the mistakes.
    """

def print_wrong():
    print("\nwrong menu number.")