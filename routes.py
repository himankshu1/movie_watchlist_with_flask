from flask import Blueprint, render_template, session, redirect, request
from forms import MovieForm


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)

@pages.route("/")
def index():
    return render_template(
        "index.html",
        title="Movies Watchlist",
    )

@pages.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = MovieForm # creating an object of MovieForm class in forms.py

    if request.method == "POST":
        pass

    return render_template("add_movie.html", title="Movies Watchlist - Add Movie", form=form)



@pages.get("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"

    return redirect(request.args.get("current_page"))