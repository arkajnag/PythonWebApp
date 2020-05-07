from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

from forms import feedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd9f86e26af8fa6271100809023e40c9b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@localhost/feedback'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'ef892873b6b0c2'
app.config['MAIL_PASSWORD'] = '28913c8435add2'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
db = SQLAlchemy(app)
mail = Mail(app)


class Feedback(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    customerName = db.Column(db.String(20), nullable=False, unique=True)
    dealerName = db.Column(db.String(20), nullable=False)
    comments = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Feedback('{self.customerName}','{self.dealerName}','{self.rating}')"


def sendMailOnSubmission(reqFeedback):
    msg = Message('Password Reset',
                  sender='sender@example.com',
                  recipients=['recipient@example.com'])
    msg.body = '''Thank you for providing your Feedback.
Your Feedback is very important for our business.
Please find your feedback comments: {reqFeedback.comments}'''
    mail.send(msg)


@app.route('/', methods=['GET', 'POST'])
def feedback():
    form = feedbackForm()
    if form.validate_on_submit():
        record = Feedback.query.filter_by(customerName=form.customerName.data).first()
        if record is None:
            reqFeedback = Feedback(customerName=form.customerName.data, dealerName=form.dealerName.data,
                                   rating=form.ratingChoice.data, comments=form.comments.data)
            db.session.add(reqFeedback)
            db.session.commit()
            flash('Thank you for feedback!!', category='success')
            print(reqFeedback)
            sendMailOnSubmission(reqFeedback)
            return redirect(url_for('feedback'))
        else:
            flash('You have already provided your feedback. Thanks again!!', category='warning')
            return redirect(url_for('feedback'))
    return render_template('feedback.html', title='Feedback', form=form)


if __name__ == '__main__':
    app.run(debug=True)
