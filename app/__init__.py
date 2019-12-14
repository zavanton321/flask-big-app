import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
lm = LoginManager()
lm.login_view = "main.login"


def create_app(configuration):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(), "config", "{0}.py".format("development"))
    app.config.from_pyfile(cfg)

    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
