from flask import Blueprint, flash, redirect, render_template, url_for
from feedback import db
from feedback.models import Feedback
from feedback.userInput.Utils import sendMailOnSubmission
from feedback.userInput.forms import feedbackForm

inputs = Blueprint('input', __name__)

@inputs.route('/', methods=['GET', 'POST'])
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
            return redirect(url_for('input.feedback'))
        else:
            flash('You have already provided your feedback. Thanks again!!', category='warning')
            return redirect(url_for('input.feedback'))
    return render_template('feedback.html', title='Feedback', form=form)