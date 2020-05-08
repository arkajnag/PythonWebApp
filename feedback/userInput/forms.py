from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

from feedback.models import Feedback


class feedbackForm(FlaskForm):
    customerName = StringField('Customer Name', validators=[DataRequired(), Length(min=4, max=20)])
    dealerName = SelectField('Dealer Name',
                             choices=[('Tom', 'Tom'), ('Jerry', 'Jerry'), ('Simon', 'Simon'), ('Maxwell', 'Maxwell')],
                             validate_choice=True)
    ratingChoice = RadioField('Rating', coerce=int, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    comments = TextAreaField('Comments about your experience', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Submit Feedback')

    # # Custom Validation function
    # def validate_customerName(self, customerName):
    #     feedback = Feedback.query.filter_by(customerName=customerName.data).first()
    #     if feedback:
    #         raise ValidationError('You have provided your feedback!! Thanks')
