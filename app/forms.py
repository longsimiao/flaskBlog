# -*- coding: utf-8 -*-
# @Time: 3/11/18 4:29 PM
# @Author: Ferras

from flask_wtf import Form
from wtforms import StringField, BooleanField, TextField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
