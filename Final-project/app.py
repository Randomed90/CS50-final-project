from flask import Flask, flash, jsonify, redirect, render_template, request, session


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    print("SUCCESS index.html")
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET" or request.method == "POST":
        return render_template("about.html")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET" or request.method == "POST":
        return render_template("profile.html")

@app.route("/projects", methods=["GET", "POST"])
def projects():
    if request.method == "GET" or request.method == "POST":
        return render_template("projects.html")

@app.route("/database", methods=["GET", "POST"])
def database():
    if request.method == "GET" or request.method == "POST":
        return render_template("database.html")

@app.route("/skills", methods=["GET", "POST"])
def skills():
    if request.method == "GET" or request.method == "POST":
        return render_template("skills.html")

@app.route("/achievements", methods=["GET", "POST"])
def achievements():
    if request.method == "GET" or request.method == "POST":
        return render_template("achievements.html")