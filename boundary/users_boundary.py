from flask import Blueprint, render_template, request, redirect, url_for
from control.create_user_control import CreateUserControl
from control.get_user_control import GetUserControl

users_bp = Blueprint("users", __name__, template_folder="../templates/users")

@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        control = CreateUserControl()
        user = control.execute(username, email, password)

        return redirect(url_for("users.get_user", user_id=user.get_id()))
    
    return render_template("users/register.html")

@users_bp.route("/<int:user_id>")
def get_user(user_id):
    control = GetUserControl()
    user = control.execute(user_id)
    return render_template("users/detail.html", user=user)