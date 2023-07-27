from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Add the user's entry into the database
        entryName = request.form.get("name")
        entryMonth = request.form.get("month")
        entryDay = request.form.get("day")
        db.execute(
            "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
            entryName,
            entryMonth,
            entryDay,
        )

        return redirect("/")

    else:
        # Display the entries in the database on index.html
        entries = db.execute("SELECT * FROM birthdays;")

        return render_template("index.html", entries=entries)
