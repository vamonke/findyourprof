import os
from flask import Flask, render_template, jsonify, redirect
from pprint import pprint
import pymysql
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth
import Prof

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.environ.get("SECRET_KEY") or "1234567"
app.register_blueprint(google_auth.app)


@app.route('/', methods=['GET'])
def home():
    if google_auth.is_logged_in():
        user = google_auth.get_current_user()
        return render_template('index.html', user=user)
    return render_template('index.html')


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
        user = google_auth.get_current_user()
        return render_template('review.html', reviews=prof_reviews, user=user)
    return render_template('index.html')


@app.route('/api/profs', methods=['GET'])
def get_profs():
    profs = Prof.get_profs()
    return jsonify(profs)

@app.route('/api/prof/<prof_id>', methods=['GET'])
def get_prof(prof_id):
    prof = Prof.get_prof(prof_id)
    return jsonify(prof)

@app.route('/prof/<prof_id>', methods=['GET'])
def prof(prof_id):
    prof = Prof.get_prof(prof_id)
    if (prof == None):
        return redirect('/')
    reviews = Prof.get_prof_reviews(prof_id)
    user = None
    if google_auth.is_logged_in():
        user = google_auth.get_current_user()
    
    return render_template('prof.html', prof=prof, user=user, reviews=reviews)

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
    return jsonify(prof_reviews)


app.run()