import pymysql.cursors
import config

connection = pymysql.connect(
host = config.host,
user = config.user,
password = config.password,
db = config.db,
charset = 'utf8',
cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "select * from student"
        sursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
