import pymysql
import uuid

def get_or_insert_user(email):
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')
    c = conn.cursor()
    c.execute("SELECT id FROM student WHERE email=%s", email)
    row = c.fetchone()

    if (row == None):
        id = str(uuid.uuid4())
        c.execute("INSERT INTO student (id, email) VALUES (%s, %s);", (id, email))
        conn.commit()
    else:
        id = row[0]

    c.close()
    conn.close()
    return id

def get_user(id):
    print('get_user', id)
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')
    c = conn.cursor()
    c.execute("SELECT * FROM student WHERE id=%s", id)
    row = c.fetchone()
    c.close()
    conn.close()

    if (row == None):
        return
    
    user = { 'id': row[0], 'email': row[1] }
    return user