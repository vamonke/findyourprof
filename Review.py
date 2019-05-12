import pymysql
import uuid

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

def get_reviews():
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')
    c = conn.cursor()
    c.execute("SELECT * from review;")

    reviews = [{
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
    return reviews

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

def add_review(review):
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')
    c = conn.cursor()

    id = str(uuid.uuid4())
    rating = review['rating'] if 'rating' in review else 'null'
    comment = review['comment'] if 'comment' in review else ''
    advice = review['advice'] if 'advice' in review else ''
    meetup = review['meetup'] if 'meetup' in review else 'null'
    studentId = review['studentId']
    profId = review['profId']
    
    query = "INSERT INTO review (id, rating, comment, advice, meetup, studentId, profId) VALUES ('%s', %s, '%s', '%s', %s, '%s', '%s');" % (id, rating, comment, advice, meetup, studentId, profId)
    print(query)
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()
    return id