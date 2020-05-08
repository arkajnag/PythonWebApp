from flask_mail import Message

from feedback import mail


def sendMailOnSubmission(reqFeedback):
    msg = Message('Password Reset',
                  sender='sender@example.com',
                  recipients=['recipient@example.com'])
    msg.body = '''Thank you for providing your Feedback.
Your Feedback is very important for our business.
Please find your feedback comments: {reqFeedback.comments}'''
    mail.send(msg)
