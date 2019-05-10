import pymysql

def get_prof(profId):
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')

    c = conn.cursor()
    c.execute("SELECT * FROM prof WHERE id = %s;", (profId))
    row = c.fetchone()

    if (len(row) == 0):
        c.close()
        conn.close()
        return None

    prof = {
        'id': row[0],
        'name': row[1],
        'school': row[2]
    }
    
    c.execute("SELECT ROUND(AVG(rating), 1) AS rating FROM review WHERE profId = %s;", (prof['id']))
    row = c.fetchone()
    if (row[0]):
        prof['rating'] = row[0]
    c.close()
    conn.close()
    return prof


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