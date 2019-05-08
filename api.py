import os
from flask import Flask, jsonify, render_template
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery
import google_auth

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or "1234567"
app.register_blueprint(google_auth.app)

@app.route('/', methods=['GET'])
def home():
    if google_auth.is_logged_in():
        user = google_auth.get_user_info()
        print(user)
        return render_template('index.html', user=user)
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
  return jsonify(result)

app.run()