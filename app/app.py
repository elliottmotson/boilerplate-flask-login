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
    if 'username' in session:
        session["userid"] = get_userid(session['username'])
        loggedin = True
        return render_template("/index.html",loggedin=loggedin,session=session)
    else:
        loggedin = False
        return render_template("/index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if database_validate(username,password):
            session['username'] = username
            logger.log("user",(username+" logged in"),"1")
            return redirect(url_for('index'))
        else:
            logger.log("user",("Invalid login to account with username " + username),"1")
            invalid = True
            return render_template("/login.html",invalid=invalid)
    return render_template("/login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if database_newuser(username,password):
            return redirect(url_for('index'))
        else:
            invalidreg = True
            return render_template("/register.html",invalidreg=invalidreg)
    return render_template("/register.html")

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route("/<string:userid>/account", methods=["GET", "POST"])
def account(userid):
    return render_template("/account.html",session=session)

def get_userid(username):
    if records.find_one({"username": username}):
        user = records.find_one({"username": username})
        userid = str(user["_id"])
        print(userid)
        return userid
    else:
        return False

def database_validate(username,password):
    if records.find_one({"username": username}):
        user = records.find_one({"username": username})
        dbhash = user["password"]
        if bcrypt.checkpw(password.encode('utf8'), dbhash):
            return True
        else:
            return False
    else:
        return False
def database_newuser(username,password):
    hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    if records.find_one({"username": username}):
        logger.log("user",("Attempted register with taken username: " + username),"1")
        return False
    else:
        records.insert_one({'username': username, 'password': hash})
        logger.log("user",("User " + username + " created."),"1")
        return True

if __name__ == "__main__":
    app.run(debug=True)
