import uuid
import pymysql

import csv

with open('review.csv', encoding='utf-8-sig') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    conn = pymysql.connect(
            db='findyourprof',
            user='root',
            passwd='',
            host='localhost')

    c = conn.cursor()
    for row in readCSV:
        print(row)
        # print(str(uuid.uuid4()))
        c.execute("INSERT INTO review (id, rating, comment, advice, meetup, studentId, profId) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                  (str(uuid.uuid4()), float(row[0]), row[1], row[2], row[3], str(uuid.uuid4()), str(uuid.uuid4())))


        conn.commit()

    c.close()
    conn.close()