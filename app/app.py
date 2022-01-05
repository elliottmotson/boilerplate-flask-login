import os
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    flash,
    url_for,
    session,
)  # noqa: E501
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = "changeme"
load_dotenv(verbose=True)

db_user = os.getenv("db_user")
db_pwd = os.getenv("db_pwd")
db_host = os.getenv("db_host")
db_database = os.getenv("db_database")

client = pymongo.MongoClient("mongodb+srv://" + db_user + ":" + db_pwd + "@" + db_host + "/" + db_database + "?retryWrites=true&w=majority")
db = client.test

class user(db.Document):
    username = db.StringField()
    password = db.StringField()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("/index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
#    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
#    if request.form.get("password") == (ADMIN_PASSWORD):
#        session["logged-in"] = True
#        return redirect(url_for("admin"))
#    else:
#        flash("Try again")
        return render_template("/login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    userdata = {
        "username": username,
        "password": password,
    }
    if database_newuser(username,password):
        return render_template("/register.html")

@app.route("/<userid>/account", methods=["GET", "POST"])
def account(userid):
    return render_template("/account.html", userid=userid)

def database_newuser(username,password):
    user(username=username, password=password).save()
    print("User " + username + " created.")
    return True

if __name__ == "__main__":
    app.run(debug=True)
