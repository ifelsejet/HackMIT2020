import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import scoped_session, sessionmaker

application = app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    if(not session):
        return render_template("index.html")
    elif(session["logged_in"] == True):
        return redirect(url_for('chatroom'))
    else:
        return render_template("index.html")