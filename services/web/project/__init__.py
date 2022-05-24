import os
from flask import Flask
from flask_sqlalchemy  import SQLAlchemy


DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
