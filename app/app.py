import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import login_required

from datetime import datetime



app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# CS50 had this... seems important
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
def location():
    # New conditions entered. Change .json and redirect to index
    if request.method == "POST":
        """ This will execute when a POST (likely NavBar button or form) is submitted to the /location route"""

        return redirect("/")
    
    # Load conditions .html
    else:
        """ Show the user their location on a zoomed minimap"""
        return render_template("location.html")


""" Requets for a tree creation (can be done from location.html for example) """
@app.route("/createTree", methods=["GET", "POST"])
@login_required
def createTree():

    if request.method == "POST":

        return redirect("/")
    
    else:
        return render_template("newTree.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    #SQLite3 query to detect listings.
    conn = sqlite3.connect('treeHub.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')
        # Ensure username was submitted
        if not request.form.get("username"):
            # TODO error: return apology("must provide username", 403)
            print("no username")
            return redirect("/login")

        # Ensure password was submitted
        elif not request.form.get("password"):
            # TODO error: return apology("must provide password", 403)
            print("no password")
            return redirect("/login")

        # Query database for username
        all = db.execute("SELECT * FROM users WHERE username = ?", username).fetchall()
        for row in all: row = dict(row)

        # TODO Ensure username exists and password is correct
        if len(row) != 1 or not check_password_hash(row[0]["hash"], password):
            print("invalid username and/or password")
            return redirect("/login")

        
        # Remember which user has logged in
        #session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    #SQLite3 query to detect listings.
    conn = sqlite3.connect('treeHub.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # May as well clear the session
    session.clear()

    # Registration submitted via form:
    if request.method == "POST":
        
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            #TODO: error message
            print("No Username")
            return redirect("/register")

        # Ensure password was submitted
        elif not password:
            #TODO: error message
            print("no Password")
            return redirect("/register")

        # Ensure password confirmed
        elif not (confirmation == password):
            #TODO: error message
            print("unconfirmed password")
            return redirect("/register")

        
        # Ensure username doesn't exist already:
        rows = db.execute("SELECT * FROM users WHERE username = ?", (username)).fetchall()
        rows = [dict(row) for row in rows]
        if len(rows) > 0: #TODO should it be 0?
            # TODO: error message
            print("username taken")
            return redirect("/register")


        # Create a new user in database:
        hashword = generate_password_hash(request.form.get("password"))
        # TODO: Add a user entry in sql:
        print(f"inserting into users: {username} and {hashword}")
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, hashword))

        return redirect("/login")

    # Or did they click a link to get here? ("GET" method)
    else:
        # They want to register
        return render_template("register.html")

if __name__ == "__main__":
    app.run()