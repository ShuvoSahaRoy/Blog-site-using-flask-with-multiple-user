import os


class Config():
    SECRET_KEY = 'super-secret-key'
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('email')
    MAIL_PASSWORD = os.environ.get('password')