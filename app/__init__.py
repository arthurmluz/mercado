from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import secrets

app_name = 'cloud-api'
db = SQLAlchemy()

conn = "postgresql://{0}:{1}@{2}:5432/{3}".format(secrets.dbpass, secrets.dbuser, secrets.dbhost, secrets.dbname)


def create_app():
    app = Flask(__name__)

    init_extensions(app)

    return app


def init_extensions(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    app.config['SECRET_KEY'] = 'SuperSecretKey'
    db.init_app(app)


