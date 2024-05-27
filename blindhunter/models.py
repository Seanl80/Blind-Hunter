from blindhunter import db


class Company(db.Model):
    # schema for the Company model
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50), unique=True, nullable=False)
    details = db.relationship("Detail", backref="company", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.company_name

class Detail(db.Model):
    # schema for the Details model
    id = db.Column(db.Integer, primary_key=True)
    detail_area = db.Column(db.String(25), unique=True, nullable=False)
    detail_description = db.Column(db.Text, nullable=False)
    detail_contact = db.Column(db.Integer, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
         return "#{0} - Detail: {1} | Contact: {2}".format(
            self.id, self.detail_area, self.detail_contact
         )



# class Review(db.Model):
#     # schema for the Review model
#     id = db.Column(db.Integer, primary_key=True)
#     review_name = db.Column(db.String(25), unique=True, nullable=False)
#     review_date = db.Column(db.Date, nullable=False)
#     review_description = db.Column(db.Text, nullable=False)
#     company_id = db.Column(db.Integer, db.ForeignKey("company.id", ondelete="CASCADE"), nullable=False)

#     def __repr__(self):
#         return self.review_name

