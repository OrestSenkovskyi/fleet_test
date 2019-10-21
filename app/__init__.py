from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import FileHandler

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import handlers

# Create and add to logging handlers custom db handler
db_handler = handlers.SQLAlchemyHandler()
db_handler.setLevel(logging.WARN)  # Only serious messages
app.logger.addHandler(db_handler)

# Create and add to logging handlers file handler
file_handler = FileHandler(filename='fleet-test.log')
file_handler.setLevel(logging.DEBUG)
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

from app import controller, models, outputs


