import pymysql

def get_prof(profId):
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')

    c = conn.cursor()
    c.execute("SELECT * from prof where id = %s;", (profId))
    row = c.fetchone()
    c.close()
    conn.close()

    if (row):
        prof = {
            'id': row[0],
            'name': row[1],
            'school': row[2]
        }
        return prof
    
    return None


def get_profs():
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')

    c = conn.cursor()
    c.execute("SELECT * from prof;")

    profs = [{
        'id': row[0],
        'name': row[1],
        'school': row[2],
    } for row in c.fetchall()]

    c.close()
    conn.close()
    return profs


def get_prof_reviews(profId):
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')

    c = conn.cursor()
    c.execute("SELECT * from review where profId = %s;", (profId))

    prof_reviews = [{
        'review_id': row[0],
        'rating': row[1],
        'comment': row[2],
        'advice': row[3],
        'meetup': row[4],
        'studentId': row[5],
        'profId': row[6]
    } for row in c.fetchall()]

    c.close()
    conn.close()
    return prof_reviews