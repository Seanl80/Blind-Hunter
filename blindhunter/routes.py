from flask import render_template, request, redirect, url_for
from blindhunter import app, db
from blindhunter.models import Company, Review


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/companies")
def companies():
    return render_template("companies.html")


@app.route("/add_company", methods=["GET", "POST"])
def add_company():
    if request.method == "POST":
        company = Company(
            company_name=request.form.get("company_name"),
            blinds_sold=request.form.get("blinds_sold"),
            contact_number=request.form.get("contact_number"),
            uk_area=request.form.get("uk_area"))
        db.session.add(company)
        db.session.commit()
        return redirect(url_for("companies"))
    return render_template("add_company.html")


@app.route("/reviews")
def reviews():
    return render_template("reviews.html")