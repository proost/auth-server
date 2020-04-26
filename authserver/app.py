from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from resources.config import SECRET_KEY


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = SECRET_KEY

@app.route("/")
def root():
    return redirect(url_for("/login"))

@app.route("/auth/login", methods=["POST"])
def auth():
        
    return redirect(url_for("home", username=username))

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/home/<username>")
@jwt_required
def home(username):
    pass

if __name__=="__main__":
    app.run('127.0.0.1')


