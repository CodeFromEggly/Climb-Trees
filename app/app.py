import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """This is the homepage"""
    
    return render_template("index.html")


@app.route("/location", methods=["GET", "POST"])
def myLocation():
    # New conditions entered. Change .json and redirect to index
    if request.method == "POST":
        """ This will execute when a POST (likely NavBar button or form) is submitted to the /location route"""

        return redirect("/")
    
    # Load conditions .html
    else:
        """ Show the user their location on a zoomed minimap"""
        return render_template("location.html")



if __name__ == "__main__":
    app.run()