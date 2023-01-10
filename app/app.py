import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import login_required

import what3words



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
    #SQLite3 query to detect listings.
    conn = sqlite3.connect('treeHub.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # Greet the user if they're logged-in
    try :        
        id = session['user_id']
        user = db.execute("SELECT username FROM users WHERE id = ?", (id,)).fetchall()
        user =  [dict(row) for row in user][0]['username']
    except:
        user = "climber"


    conn.close()
    return render_template("index.html", user=user)


@app.route("/location", methods=["GET", "POST"])
def location():
    # New conditions entered. Change .json and redirect to index
    if request.method == "POST":
        """ """

        return redirect("/")
    
    # Load conditions .html
    else:
        """ Show the user their location on a zoomed minimap"""

        # Plot tree locations:
        conn = sqlite3.connect('treeHub.db')
        conn.row_factory = sqlite3.Row
        db = conn.cursor()

        trees = db.execute("SELECT * FROM trees").fetchall()
        trees = [dict(row) for row in trees]




        from APIkeys import gmaps
        conn.close()
        return render_template("location.html",API=gmaps, trees=trees)


""" Requets for a tree creation (can be done from location.html for example) """
@app.route("/newTree", methods=["GET", "POST"])
@login_required
def newTree():

    if request.method == "POST":
        
        # Process form data:

        # Load submission
        w3w = request.form.get('w3w')
        if w3w == '':
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')
            #TODO:
            w3w = "no.result.yet"
        else:
            # Get coords from code using API
            #TODO:
            latitude = 0
            longitude = 0
            
        

        grade = request.form.get('grade')

        # TODO Check submission:
        
        # Add tree to database:

        #SQLite3 query to detect listings.
        conn = sqlite3.connect('treeHub.db')
        conn.row_factory = sqlite3.Row
        db = conn.cursor()

        # TODO: Check if there exists that tree already.

        # Table takes numeric entries:
        latitude = float(latitude)
        longitude= float(longitude)
        grade = int(grade)

        # INSERT NEW TREE
        db.execute("INSERT INTO trees"
        "(latitude, longitude, w3w, grade, planter)"
        "VALUES (?,?,?,?,?)",(latitude, longitude, w3w, grade, session['user_id']))
        conn.commit()





        conn.close()
        return redirect("/")
    
    else:
        return render_template("newTree.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        #SQLite3 query to detect listings.
        conn = sqlite3.connect('treeHub.db')
        conn.row_factory = sqlite3.Row
        db = conn.cursor()

        username = request.form.get('username')
        password = request.form.get('password')
        # Ensure username was submitted
        if not request.form.get("username"):
            print("no username")
            return redirect("/login?message=Please+provide+username")

        # Ensure password was submitted
        if not request.form.get("password"):
            print("no password")
            return redirect("/login?message=Please+provide+password")

        # Query database for username
        all = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()
        all = [dict(row) for row in all]
        print(f"All is:::: {all}")

        if len(all) != 1 or not check_password_hash(all[0]["hash"], password):
            print("invalid username and/or password")
            return redirect("/login?message=Invalid+username+or+password")

                # Remember which user has logged in
        print(f"logging in with ID: {all[0]['id']}")
        session["user_id"] = all[0]["id"]

        conn.close()
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
    

    # Registration submitted via form:
    if request.method == "POST":

        #SQLite3 query to detect listings.
        conn = sqlite3.connect('treeHub.db')
        conn.row_factory = sqlite3.Row
        db = conn.cursor()

        # May as well clear the session
        session.clear()
        
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            print("No Username")
            return redirect("/register?message=Please+provide+username")

        # Ensure password was submitted
        elif not password:
            print("no Password")
            return redirect("/register?message=Please+provide+password")

        # Ensure password confirmed
        elif not (confirmation == password):
            print("unconfirmed password")
            return redirect("/register?message=Passwords+don't+match")

        
        # Ensure username doesn't exist already:
        rows = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()
        rows = [dict(row) for row in rows]
        if len(rows) > 0:
            print("username taken")
            return redirect("/register?message=Username+taken")


        # Create a new user in database:
        hashword = generate_password_hash(request.form.get("password"))

        print(f"inserting into users: {username} and {hashword}")
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, hashword))
        conn.commit()

        conn.close()

        return redirect("/login")

    # Or did they click a link to get here? ("GET" method)
    else:
        # They want to register
        return render_template("register.html")



if __name__ == "__main__":
    app.run()