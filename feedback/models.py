from feedback import db


class Feedback(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    customerName = db.Column(db.String(20), nullable=False, unique=True)
    dealerName = db.Column(db.String(20), nullable=False)
    comments = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Feedback('{self.customerName}','{self.dealerName}','{self.rating}')"
