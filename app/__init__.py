from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# add console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# add fileHandler
fileHander = RotatingFileHandler("logs.log", backupCount=10, maxBytes=2048)
fileHander.setFormatter(logFormatter)
logger.addHandler(fileHander)


app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
# app.app_context().push()

migrate = Migrate(app, db)


from app import views, models