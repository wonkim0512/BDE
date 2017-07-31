#-*- coding: utf-8 -*-
import pymysql.cursors
import config

connection = pymysql.connect(
host = config.host,
user = config.user,
password = config.password,
db = config.db,
charset = 'utf8',
cursorclass = pymysql.cursors.DictCursor)

'''
try:
    with connection.cursor() as cursor:
        sql = "select * from performances;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()
'''

'''
try: # different grammar from selection
    with connection.cursor() as cursor:
        sql = "insert into buildings values('3','Seongnam Art Center',\
        'Seongnam',8,Null)"
        cursor.execute(sql)
        connection.commit()


finally:
    connection.close()
'''

try:
    with connection.cursor() as cursor:
        sql = "insert into performances values('3','Les Miserables',\
        'Musical', 70000, Null)"
        cursor.execute(sql)
        cursor.execute(sql)
        connection.commit()

finally:
    connection.close()
