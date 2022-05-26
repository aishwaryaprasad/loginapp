import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

db = SQLAlchemy(app)
