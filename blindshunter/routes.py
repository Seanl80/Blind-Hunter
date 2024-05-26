from flask import render_template
from blindshunter import app, db
from blindshunter.models import Company, Review


@app.route("/")
def home():
    return render_template("home.html")