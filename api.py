import os
from flask import Flask, render_template, jsonify, redirect, request
from pprint import pprint
import pymysql
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth
import Prof
import Review

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.environ.get("SECRET_KEY") or "1234567"
app.register_blueprint(google_auth.app)

@app.route('/', methods=['GET'])
def home():
    user = None
    if google_auth.is_logged_in():
        user = google_auth.get_current_user()
    return render_template('index.html', user=user)

@app.route('/review', methods=['GET'])
def view_review():
    reviews = Review.get_reviews()
    user = None
    if google_auth.is_logged_in():
        user = google_auth.get_current_user()
    return render_template('review.html', reviews=reviews, user=user)

@app.route('/prof/<prof_id>', methods=['GET'])
def view_prof(prof_id):
    prof = Prof.get_prof(prof_id)
    if (prof == None):
        return redirect('/')
    reviews = Review.get_prof_reviews(prof_id)
    user = None
    if google_auth.is_logged_in():
        user = google_auth.get_current_user()
    return render_template('prof.html', prof=prof, user=user, reviews=reviews)

# API endpoints

@app.route('/api/profs', methods=['GET'])
def get_profs():
    profs = Prof.get_profs()
    return jsonify(profs)

@app.route('/api/prof/<prof_id>', methods=['GET'])
def get_prof(prof_id):
    prof = Prof.get_prof(prof_id)
    return jsonify(prof)

@app.route('/api/review', methods=['GET'])
def get_review():
    reviews = Review.get_reviews()
    return jsonify(reviews)

@app.route('/api/review', methods=['POST'])
def post_review():
    review = request.json
    
    # rating = json['rating'] if 'rating' in json else None
    # comment = json['comment'] if 'comment' in json else None
    # advice = json['advice'] if 'advice' in json else None
    # meetup = json['meetup'] if 'meetup' in json else None
    # studentId = json['studentId']
    # profId = json['profId']

    id = Review.add_review(review)
    return id

app.run()