from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from authserver.resources.config import SECRET_KEY
from authserver.templates.forms import LoginForm


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = SECRET_KEY

@app.route("/")
def root():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = LoginForm(request.form)
        return render_template("login.html", form=form)

@app.route("/home/<username>")
@jwt_required
def home(username):
    pass

if __name__=="__main__":
    app.run('127.0.0.1')


