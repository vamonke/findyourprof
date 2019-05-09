import os
import flask
from pprint import pprint
import pymysql
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.environ.get("SECRET_KEY") or "1234567"
app.register_blueprint(google_auth.app)




@app.route('/', methods=['GET'])
def home():
    if google_auth.is_logged_in():
        user = google_auth.get_current_user()
        return flask.render_template('index.html', user=user)
    return flask.render_template('index.html')


@app.route('/review', methods=['GET'])
def view_review():
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')

    c = conn.cursor()
    c.execute("SELECT * from review;")

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

    if google_auth.is_logged_in():
        user = google_auth.get_user_info()
        return render_template('review.html', reviews=prof_reviews, user=user)
    return render_template('index.html')


@app.route('/api/profs', methods=['GET'])
def api_breaking():
  result = [
    {
      'id': '123',
      'name': 'Varick Lim',
      'school': 'School of Electrical and Electronic Engineering',
      'research': ['topic1', 'topic2', 'topic3', 'topic4']
    }
  ]
  return flask.jsonify(result)

@app.route('/api/review', methods=['GET'])
def get_review():
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')

    c = conn.cursor()
    c.execute("SELECT * from review;")

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
    return flask.jsonify(prof_reviews)


app.run()