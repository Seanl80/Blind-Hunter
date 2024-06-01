from flask import render_template, request, redirect, url_for, session
from sqlalchemy import desc
from blindhunter import app, db
from blindhunter.models import Company, Review

from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/companies")
def companies():
    companies = list(Company.query.order_by(Company.company_name).all())
    return render_template("companies.html", companies=companies)


@app.route("/add_company", methods=["GET", "POST"])
def add_company():
    if request.method == "POST":
        company = Company(
            company_name=request.form.get("company_name"),
            location=request.form.get("location"),
            area=request.form.get("area"),
            email=request.form.get("email"),
            phone=request.form.get("phone"),
        )
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


@app.route("/delete_company/<int:company_id>", methods=["GET", "POST"])
def delete_company(company_id):
    company = Company.query.get_or_404(company_id)
    db.session.delete(company)
    db.session.commit()
    return redirect(url_for("companies"))


@app.route("/reviews")
def reviews():
    reviews = list(Review.query.order_by(desc(Review.date)).all())
    return render_template("reviews.html", reviews=reviews)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = Review(
            review_name=request.form.get("review_name"),
            company_id=request.form.get("company_id"),
            date=request.form.get("date"),
            description=request.form.get("description"),
            )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("add_review.html")


@app.route('/edit_review/<int:review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)
    if request.method == 'POST':
        review.review_name = request.form.get("review_name")
        db.session.commit()
        return redirect('reviews')
    return render_template('edit_review.html', review=review)


@app.route('/delete_review/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect('reviews')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password, role='user')
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash('Login successful!', 'success')
            return redirect(url_for('companies'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('home.html')