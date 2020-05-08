from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from feedback.config import Config, ProductionConfig

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    from feedback.userInput.inputRoute import inputs
    from feedback.errors.handlers import errors

    db.init_app(app)
    mail.init_app(app)
    app.register_blueprint(inputs)
    app.register_blueprint(errors)
    return app



