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

@app.route('/api/review/<prof_id>', methods=['GET'])
def get_review(prof_id):
    conn = pymysql.connect(
        db='findyourprof',
        user='root',
        passwd='',
        host='localhost')

    c = conn.cursor()
    c.execute("SELECT * from review WHERE prof_id = %s;", (prof_id))

    prof_reviews = [{
        'prof_id': row[0],
        'review_id': row[1],
        'rating': row[2],
        'review': row[3],
        'recommended': row[4]
    } for row in c.fetchall()]


    c.close()
    conn.close()
    return jsonify(prof_reviews)


app.run()