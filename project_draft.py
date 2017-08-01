#-*- coding: utf-8 -*-
import pymysql.cursors
import config
import sys

connection = pymysql.connect(
host = config.host,
user = config.user,
password = config.password,
db = config.db,
charset = 'utf8',
cursorclass = pymysql.cursors.DictCursor)


print("================================================\n\
1.  print all buildings \n\
2.  print all performances \n\
3.  print all audiences \n\
4.  insert a new building \n\
5.  remove a building \n\
6.  insert a new performance \n\
7.  remove a performance \n\
8.  insert a new audience \n\
9.  remove a audience \n\
10. assign a performance to a building \n\
11. book a performances \n\
12. print all performances wich assigned at a building \n\
13. print all audiences who booked for a performance \n\
14. print ticket booking status of a performance \n\
15. exit \n\
================================================")

number = eval(input("Select your action: "))

'''
def button(number):
    for i in range(1, 16):
        if number == i:
            this_module = sys.modules[__name__]
            getattr(this_module, "f"+str(i))()
'''
def button(number):

    if number == 1:
        f1()

    if number == 2:
        f2()

    if number == 3:
        f3()

    if number == 4:
        bldg_name = input("Building name: ")
        bldg_loc = input("Building location: ")
        bldg_capacity = int(input("Building capacity: "))
        f4(bldg_name, bldg_loc, bldg_capacity)

    if number == 5:
        bldg_name = input("Building name: ")
        f5(bldg_name)

    if number == 6:
        perf_name = input("Performance name: ")
        perf_type= input("Performance type: ")
        perf_price = int(input("Performance price: "))
        f6(perf_name, perf_type, perf_price)

    if number == 7:
        perf_name = input("Performance name: ")
        f7(perf_name)

    if number == 8:
        aud_name = input("Audience name: ")
        aud_gender = input("Audience gender: ")
        aud_age = int(input("Audience age: "))
        f8(aud_name, aud_gender, aud_age)

    if number == 9:
        aud_name = input("Audience name: ")
        f9(aud_name)

    if number == 10:
        bldg_id = int(input("Building id: "))
        perf_id = int(input("Performance id: "))
        f10(bldg_id, perf_id)

    if number == 11:
        f11()

    if number == 12:
        f12()

    if number == 13:
        f13()

    if number == 14:
        f14()

    if number == 15:
        f15()

def f1():
    with connection.cursor() as cursor:
        sql = "select * from buildings;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)


def f2():
    with connection.cursor() as cursor:
        sql = "select * from performances;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)


def f3():
    with connection.cursor() as cursor:
        sql = "select * from audiences;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("ID\tName\t\tGender\tAge")
        for row in result:
            print(row["aud_id"], "\t" + row["name"]+ "\t" + row["gender"]+ "\t", row["age"])


def f4(bldg_name, bldg_loc, bldg_capacity):
    with connection.cursor() as cursor:
        sql = "insert into buildings(name, location, capacity) \
        values(%s, %s, %s);"
        cursor.execute(sql,(bldg_name,bldg_loc,bldg_capacity))
        connection.commit()

def f5(bldg_name):
    with connection.cursor() as cursor:
        sql = "select name from buildings;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if bldg_name in result:
            with connection.cursor() as cursor:
                sql = "delete from buildings where name = %s"
                cursor.execute(sql,(bldg_name))
                connection.commit()

        else:
            print("There is no building like that.")

def f6(perf_name, perf_type, perf_price):
    with connection.cursor() as cursor:
        sql = "insert into performances(name, type, price) \
        values(%s, %s, %s)"
        cursor.execute(sql,(perf_name, perf_type, perf_price))
        connection.commit()

def f7(perf_name):
    with connection.cursor() as cursor:
        sql = "select name from performances;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if bldg_name in result:
            with connection.cursor() as cursor:
                sql = "delete from performances where name = %s"
                cursor.execute(sql,(perf_name))
                connection.commit()

        else:
            print("There is no perfomance like that.")


def f8(aud_name, aud_gender, aud_age):
    with connection.cursor() as cursor:
        sql = "insert into audiences(name, gender, age) \
        values(%s, %s, %s)"
        cursor.execute(sql,(aud_name, aud_gender, aud_age))
        connection.commit()

def f9(aud_name):
    with connection.cursor() as cursor:
        sql = "select name from audiences;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if bldg_name in result:
            with connection.cursor() as cursor:
                sql = "delete from audiences where name = %s"
                cursor.execute(sql,(aud_name))
                connection.commit()

        else:
            print("There is no audience like that.")

def f10(bldg_id, perf_id):
    with connection.cursor() as cursor:
        sql = "select perform_id from performances;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if perf_id in result:
            print("This performance is already placed;")


        else:
            with connection.cursor() as cursor:
                sql = "insert into performances(bldg_id) values(%s);"
                cursor.execute(sql,(bldg_id))
                connection.commit()

# def f11

def f12():
    with connection.cursor() as cursor:
        sql = "select * from buildings join performances using(bldg_id);"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)


def f15():
    print("Good bye!;")
    connection.close()

button(number)
