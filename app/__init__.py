from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from applicationinsights.flask.ext import AppInsights
import os
import warnings

APP_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(APP_DIR, '../static/build/static') # Where your webpack build output folder is
TEMPLATE_FOLDER = os.path.join(APP_DIR, '../static/build') # Where your index.html file is located

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config.from_object('app.config.ProductionConfig')

if app.config.get('APPINSIGHTS_INSTRUMENTATIONKEY', None):
    appinsights = AppInsights(app)
else:
    warnings.warn("Application Insights not configured. Please set the environment variable 'APPINSIGHTS_INSTRUMENTATIONKEY' to enable...")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)