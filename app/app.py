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
        if database_validate(username,password):
            return redirect(url_for('index'))
    return render_template("/login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if database_newuser(username,password):
            return redirect(url_for('index'))
    return render_template("/register.html")

@app.route("/<userid>/account", methods=["GET", "POST"])
def account(userid):
    return render_template("/account.html", userid=userid)

def database_validate(username,password):
    return True

def database_newuser(username,password):
    hash = bcrypt.hashpw(password.encode(encoding='UTF-8'), bcrypt.gensalt())
    userinput = {'username': username, 'password':hash}
    records.insert_one(userinput)
    text = ("User " + username + " created.")
    logger.log("system",userinput,"1")
    logger.log("user",text,"1")
    user_true = True
    return True

if __name__ == "__main__":
    app.run(debug=True)
