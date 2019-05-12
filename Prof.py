import pymysql

def getMeetup(days):
    if (days == None):
        return 'Depends'
    elif days < 5: # 1-4
        return 'Once every few days'
    elif days < 11: # 5-10
        return 'Once a week'
    elif days < 20: # 11-19
        return 'Once every 2 weeks'
    elif days < 50: # 20-49
        return 'Once a month'
    elif days < 100: # 50-99
        return 'Once every few months'
    elif days < 150: # 100-149
        return 'Once per semester'
    elif days < 300: # 150-299
        return 'Once'
    else:
        return None

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
    
    query = "SELECT ROUND(AVG(rating), 1) AS rating, AVG(meetup) AS meetup FROM review WHERE profId = '%s';" % (prof['id'])
    print(query)

    c.execute(query)
    row = c.fetchone()
    if (row):
        prof['rating'] = row[0]
        prof['meetup'] = getMeetup(row[1])
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
        'meetup': getMeetup(row[4]),
        'studentId': row[5],
        'profId': row[6]
    } for row in c.fetchall()]

    c.close()
    conn.close()
    return prof_reviews