from flask import Flask, jsonify, render_template
# import pymongo

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

app.run()