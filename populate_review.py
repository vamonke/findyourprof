import uuid
import pymysql

# conn = pymysql.connect(
#         db='findyourprof',
#         user='root',
#         passwd='',
#         host='localhost')
#
# c = conn.cursor()
# c.execute("SELECT * from review WHERE prof_id = %s;", (prof_id))
#
# prof_reviews = [{
#     'prof_id': row[0],
#     'review_id': row[1],
#     'rating': row[2],
#     'review': row[3],
#     'recommended': row[4]
# } for row in c.fetchall()]
#
#
# c.close()
# conn.close()
# return jsonify(prof_reviews)
# >>> import uuid
# >>> uuid.uuid4()
# UUID('bd65600d-8669-4903-8a14-af88203add38')
# >>> str(uuid.uuid4())
# 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'
# >>> uuid.uuid4().hex
# '9fe2c4e93f654fdbb24c02b15259716c'

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
        print(float(row[0]))
        # print(str(uuid.uuid4()))
        c.execute("INSERT INTO review (id, rating, comment, advice, meetup, studentId, profId) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                  (str(uuid.uuid4()), float(row[0]), row[1], row[2], row[3], str(uuid.uuid4()), str(uuid.uuid4())))


        conn.commit()

        # print(row[0],row[1],row[2],)

    c.close()
    conn.close()