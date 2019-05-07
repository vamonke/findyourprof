from flask import Flask, jsonify, render_template
# import pymongo
from pprint import pprint
import pymysql

app = Flask(__name__)
app.config["DEBUG"] = True

# mongoCLient = pymongo.MongoClient("mongodb://localhost:27017/")
# db = mongoCLient["fyfypp"]
# users = db["users"]
# profs = db["profs"]

@app.route('/', methods=['GET'])
def home():
  return render_template("index.html")

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
  return jsonify(result)

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