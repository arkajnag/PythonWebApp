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
    SQLALCHEMY_DATABASE_URI = 'postgres://temzjchwbahagg' \
                              ':1bab62cebad3e2a8a5fb7d6a681c2ca3fe9b7025594b36fcdc4333677280b0a7@ec2-35-171-31-33' \
                              '.compute-1.amazonaws.com:5432/df4pt0e86bsho '
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'ef892873b6b0c2'
    MAIL_PASSWORD = '28913c8435add2'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
