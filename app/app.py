from flask import (
    Flask,
    render_template,
    redirect,
    request,
    flash,
    url_for,
    session,
)  # noqa: E501

app = Flask(__name__)
app.secret_key = "changeme"

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
#    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
#    if request.form.get("password") == (ADMIN_PASSWORD):
#        session["logged-in"] = True
#        return redirect(url_for("admin"))
#    else:
#        flash("Try again")
        return render_template("/register.html")

@app.route("/<userid>/account", methods=["GET", "POST"])
def account(userid):

    return render_template("/account.html", userid=userid)
