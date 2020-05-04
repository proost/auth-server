from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_jwt_extended import (
    JWTManager, jwt_refresh_token_required, get_jwt_identity, jwt_required
)

from authserver.entity.user import UserFromView
from authserver.resources.config import SECRET_KEY
from authserver.templates.forms import LoginForm
from authserver.service_layer.user_service import UserService

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = SECRET_KEY
jwt = JWTManager(app)

@app.route("/")
def root():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = LoginForm(request.form)
        return render_template("login.html", form=form)
    
    if request.method == "POST":
        user = UserFromView(
            name="tester0",
            email=request.form.get("email", type=str),
            password=request.form.get("password", type=str)
        )
        #token = UserService.login(user)
        return redirect(url_for("home", username=user.name))
 
@app.route("/home/", defaults={"username": None})
@app.route("/home/<username>")
@jwt_required
def home(username=None):
    current_user = get_jwt_identity()
    if current_user:
        return render_template("loginsuccess.html", username=username)
    else:
        return redirect(url_for("login"))
    
@app.route("/register")
def register():
    pass


if __name__=="__main__":
    app.run('127.0.0.1')


