from blindhunter import db


class Company(db.Model):
    # schema for the Company model
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    area = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    reviews = db.relationship("Review", backref="company", cascade="all, delete", lazy=True)

    def __repr__(self):
         return f"{self.company_name} - {self.location}, {self.area}, {self.email}, {self.phone}"


class Review(db.Model):
    # schema for the Review model
    id = db.Column(db.Integer, primary_key=True)
    review_name = db.Column(db.String(25), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id", ondelete="CASCADE"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=False)
   
    def __repr__(self):
         return f"{self.review_name} - {self.company_id}, {self.date}, {self.description}"

class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    