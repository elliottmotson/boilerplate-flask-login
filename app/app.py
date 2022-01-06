import os
import urllib.parse
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    flash,
    url_for,
    session,
)  # noqa: E501
import bcrypt
from flask_mongoengine import MongoEngine
import pymongo
from dotenv import load_dotenv
import logger
import time
from bson import json_util
import json

app = Flask(__name__)
load_dotenv(verbose=True)

app.secret_key = os.getenv("secret_key")


db_user = os.getenv("db_user")
db_pwd = urllib.parse.quote_plus(os.getenv("db_pwd"))
db_host = os.getenv("db_host")
db_database = os.getenv("db_database")

client = pymongo.MongoClient("mongodb+srv://" + db_user + ":" + db_pwd + "@" + db_host + "/" + db_database + "?retryWrites=true&w=majority")
db = client.get_database(db_database)
records = db.users

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("/index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if database_validate(username,password): #Login form validation
            return redirect(url_for('index'))
    return render_template("/login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if database_newuser(username,password):
            print("LOGGED IN")
            return redirect(url_for('index'))
        else:
            invalidlogin = True
            return render_template("/register.html",invalidlogin=invalidlogin)
    return render_template("/register.html")

@app.route("/<userid>/account", methods=["GET", "POST"])
def account(userid):
    return render_template("/account.html", userid=userid)

def database_validate(username,password):##############################BROKEN

    #dbhash = user["password"]
    userinput = ({"username": username})
    user = records.find_one(userinput)
    userlist = list(user)
    userdata = json.dumps(userlist["password"])
    print(userdata[2])
    return True
    #if bcrypt.hashpw(password, dbhash) == dbhash:
    #    return True
    #else:
    #    return False

def database_newuser(username,password):
    hash = bcrypt.hashpw(password.encode(encoding='UTF-8'), bcrypt.gensalt())
    userinput = {'username': username, 'password':hash}
    records.insert_one(userinput)
    text = ("User " + username + " created.")
    logger.log("system",userinput,"1")
    logger.log("user",text,"1")
    return True

if __name__ == "__main__":
    app.run(debug=True)
