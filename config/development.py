import os

DEBUG = True
SECRET_KEY = "SOME_KEY"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.dirname(__file__), "../data-dev.sqlite3")
