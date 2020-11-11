from flask import Flask, session, request
from flask_session import Session
import json
from flask_cors import CORS
app = Flask(__name__)
app.secret_key = '786dsadhalhd7sady8asdhyaksdnas9'
CORS(app) 
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/saveUser', methods=['POST'])
def saveUser():
    data = request.get_json()
    if "users" in session:
        print(session["users"])
        session["users"].append(data)
    else:
        session["users"] = []
    return ""

@app.route('/', methods=['GET'])
def default():
    return "Hello world"


@app.route('/flushSession', methods=['GET'])
def flushSession():
    if "users" in session:
        session["users"] = []
    else:
        session["users"] = []
    return ""


@app.route('/getUsersInfo', methods=['GET'])
def getUserInfo():
    if "users" in session:
        return json.dumps(session["users"])
    else:
        return ""


if __name__== "__main__":
    app.run()