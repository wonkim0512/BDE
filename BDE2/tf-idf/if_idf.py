from connection import *
from inverted_index import *

# Query 1: ID=41631770인 text의 단어 also 에 대한 TF-IDF

sql1 = 'SELECT text FROM bde10.wiki WHERE id = 41631770'
cursor.execute(sql1)
text1 = cursor.fetchall()
atf1 = 0
word_numbers1 = len(text1[0]['text'].split())

for word in text1[0]['text'].split():
    if word == "also":
        atf1 += 1


# Query 2: ID=6688599인 text의 단어 debut에 대한 TF-IDF

sql2 = 'SELECT text FROM bde10.wiki WHERE id = 6688599'
cursor.execute(sql2)
text2 = cursor.fetchall()
atf2 = 0
word_numbers2 = len(text2[0]['text'].split())

for word in text2[0]['text'].split():
    if word == "debut":
        atf2 += 1


# Query 3: ID=13794826인 text의 단어 language에 대한 TF-IDF

sql3 = 'SELECT text FROM bde10.wiki WHERE id = 13794826'
cursor.execute(sql3)
text3 = cursor.fetchall()
atf3 = 0
word_numbers3 = len(text3[0]['text'].split())

for word in text3[0]['text'].split():
    if word == "language":
        atf3 += 1



# TF-IDF calculation
import numpy as np

tf1 = np.log(1 + (atf1/word_numbers1))
sql1 = "SELECT count(*) FROM bde10.inverted_wiki WHERE term = 'also'"
cursor.execute(sql1)
inverted_index1 = cursor.fetchone()['count(*)']
print("TF-IDF for query1:", tf1/inverted_index1)


tf2 = np.log(1 + (atf2/word_numbers2))
sql2 = "SELECT count(*) FROM bde10.inverted_wiki WHERE term = 'debut'"
cursor.execute(sql2)
inverted_index2 = cursor.fetchone()["count(*)"]
print("TF-IDF for query2:", tf2/inverted_index2)


tf3 = np.log(1 + (atf3/word_numbers3))
sql3 = "SELECT count(*) FROM bde10.inverted_wiki WHERE term = 'language'"
cursor.execute(sql3)
inverted_index3 = cursor.fetchone()["count(*)"]
print("TF-IDF for query3:", tf3/inverted_index3)