from flask import render_template, request, redirect, url_for
from blindhunter import app, db
from blindhunter.models import Company, Detail


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/companies")
def companies():
    companies = list(Company.query.order_by(Company.company_name).all())
    return render_template("companies.html", companies=companies)


@app.route("/add_company", methods=["GET", "POST"])
def add_company():
    if request.method == "POST":
        company = Company(company_name=request.form.get("company_name"))
        db.session.add(company)
        db.session.commit()
        return redirect(url_for("companies"))
    return render_template("add_company.html")


@app.route("/edit_company/<int:company_id>", methods=["GET", "POST"])
def edit_company(company_id):
    company = Company.query.get_or_404(company_id)
    if request.method == "POST":
        company.company_name = request.form.get("company_name")
        db.session.commit()
        return redirect(url_for("companies"))
    return render_template("edit_company.html", company=company)


@app.route("/reviews")
def reviews():
    return render_template("reviews.html")