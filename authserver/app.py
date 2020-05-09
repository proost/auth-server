from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_jwt_extended import (
    JWTManager,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    set_refresh_cookies
)

from authserver.entity.user import User
from authserver.resources.config import SECRET_KEY
from authserver.templates.forms import LoginForm
from authserver.service_layer.user_service import UserService


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = SECRET_KEY
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
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
        user = User(
            email=request.form.get("email", type=str),
            password=request.form.get("password", type=str)
        )
        data = UserService().authenticate_user(user)
        
        print(data)
        if data:
            res = jsonify({
                "msg": "Login success"
            })
            set_access_cookies(res, data["access_token"])
            set_refresh_cookies(res, data["refresh_token"])
            return res, 200
        else:
            return jsonify({
                "msg": "Not User or Wrong user"
            }), 400

@app.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    new_token = UserService().refresh_token(current_user)
    res = jsonify({
        "msg": "fresh success"
    })
    set_access_cookies(res, new_token)
    return res, 200

@jwt.expired_token_loader
def callback_expired_token(expired_token):
    return redirect(url_for("refresh"))



if __name__=="__main__":
    app.run('127.0.0.1')


