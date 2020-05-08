
class Config:
    SECRET_KEY = 'd9f86e26af8fa6271100809023e40c9b'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:admin@localhost/feedback'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'ef892873b6b0c2'
    MAIL_PASSWORD = '28913c8435add2'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

class ProductionConfig:
    SECRET_KEY = 'd9f86e26af8fa6271100809023e40c9b'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:admin@localhost/feedback'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'ef892873b6b0c2'
    MAIL_PASSWORD = '28913c8435add2'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False