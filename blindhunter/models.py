from blindhunter import db


class Company(db.Model):
    # schema for the Company model
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    blinds = db.Column(db.String(200), nullable=False)

    def __repr__(self):
         return f"{self.company_name} - {self.address}, {self.location}, {self.email}, {self.phone}, {self.blinds}"


class Review(db.Model):
    # schema for the Review model
    id = db.Column(db.Integer, primary_key=True)
    review_name = db.Column(db.String(25), unique=True, nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    review_description = db.Column(db.Text, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
         return "#{0} - Detail: {1} | Contact: {2}".format(
            self.id, self.review_name, self.review_date
         )
