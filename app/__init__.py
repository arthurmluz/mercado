from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from app.adaptadores.controllers import register_routes

import secrets

app_name = 'cloud-api'
db = SQLAlchemy()

conn = "postgresql://{0}:{1}@{2}:5432/{3}".format(secrets.dbpass, secrets.dbuser, secrets.dbhost, secrets.dbname)

root_blueprint = Blueprint('root_blueprint', __name__)
root_api = Api(root_blueprint, title='API mercado', version='1.0', description='Mercado')


def create_app():
    app = Flask(__name__)

    init_extensions(app)

    init_blueprints(app)

    return app


def init_extensions(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    app.config['SECRET_KEY'] = 'SuperSecretKey'
    db.init_app(app)


def init_blueprints(app):
    app.register_blueprint(root_blueprint)

    register_routes(root_api)

