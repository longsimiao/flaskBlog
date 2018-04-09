# -*- coding: utf-8 -*-
# @Time: 3/11/18 3:55 PM
# @Author: Ferras

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
