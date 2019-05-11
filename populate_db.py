import uuid
import pymysql
import random

import csv

conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')

c = conn.cursor()

profIds = []

with open('prof.csv', encoding='utf-8-sig') as csvfile:
    school = 'School of Electrical and Electronic Engineering'
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        profId = str(uuid.uuid4())
        c.execute("INSERT INTO prof (id, name, school) VALUES (%s, %s, %s);", (profId, row[0], school))
        profIds.append(profId)
        conn.commit()

# print(profIds)

with open('review.csv', encoding='utf-8-sig') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        studentId = str(uuid.uuid4())
        profId = random.choice(profIds)
        c.execute("INSERT INTO student (id, email) VALUES (%s, %s);", (studentId, str(row[0])))
        c.execute("INSERT INTO review (id, rating, comment, advice, meetup, studentId, profId) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                  (str(uuid.uuid4()), float(row[1]), row[2], row[3], row[4], studentId, profId))

        conn.commit()

c.close()
conn.close()