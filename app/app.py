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

app = Flask(__name__)
app.secret_key = "changeme"

app.config['MONGODB_SETTINGS'] = {
    'db': 'database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

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
