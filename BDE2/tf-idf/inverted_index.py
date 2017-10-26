from connection import *

# create table
sql = "DROP TABLE IF EXISTS inverted_wiki;" \
      "CREATE TABLE inverted_wiki(" \
      "term varchar(1000), id int(11));"
cursor.execute(sql)


words = ["debut", "two", "language", "also"]

for word in words:
    sql = 'SELECT id FROM bde10.wiki WHERE text like "%{}%"'.format(word)
    cursor.execute(sql)
    rows = cursor.fetchall()
    # insert data into inverted_wiki
    for row in rows:
        sql = "INSERT INTO inverted_wiki(term, id) VALUES(%s, %s)"
        cursor.execute(sql, (word, row["id"]))
        connection.commit()

