from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from feedback.config import Config

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from feedback.userInput.inputRoute import inputs

    db.init_app(app)
    mail.init_app(app)
    app.register_blueprint(inputs)
    return app



