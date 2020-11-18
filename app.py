from flask import Flask, session, request
from flask_session import Session
import json
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)
app.secret_key = '786dsadhalhd7sady8asdhyaksdnas9'
CORS(app) 
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

MAIN_FILE_PATH = "DATA_.json"

@cross_origin()
@app.route('/saveUser', methods=['POST'])
def saveUser():
    data = request.get_json()
    if os.path.exists(MAIN_FILE_PATH):
        data_so_far = dict()
        with open(MAIN_FILE_PATH) as json_file:
            data_so_far = json.load(json_file)
        os.remove(MAIN_FILE_PATH)
        print(data_so_far)
        data_so_far["users"].append(data)
        with open(MAIN_FILE_PATH,"w") as f:
            f.write(json.dumps(data_so_far))
    else:
        ew = dict()
        with open(MAIN_FILE_PATH,"w") as f:
            ew["users"] = []
            ew["users"].append(data)
            e_json = json.dumps(ew)
            f.write(e_json)
    return ""

@cross_origin()
@app.route('/', methods=['GET'])
def default():
    return "Hello world"

@cross_origin()
@app.route('/flushSession', methods=['GET'])
def flushSession():
    if os.path.exist(MAIN_FILE_PATH):
         os.remove(MAIN_FILE_PATH)
    return ""

@cross_origin()
@app.route('/getUsersInfo', methods=['GET'])
def getUserInfo():
    if os.path.exists(MAIN_FILE_PATH):
        with open(MAIN_FILE_PATH) as json_file:
            data = json.load(json_file)
            return json.dumps(data["users"])
    else:
        return ""


if __name__== "__main__":
    app.run()