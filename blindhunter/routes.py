from flask import render_template
from blindhunter import app, db
from blindhunter.models import Company, Review


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/companies")
def companies():
    return render_template("companies.html")


@app.route("/reviews")
def reviews():
    return render_template("reviews.html")