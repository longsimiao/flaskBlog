# -*- coding: utf-8 -*-
# @Time: 3/11/18 3:57 PM
# @Author: Ferras

from flask import render_template, flash, redirect

from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data +
              '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form,
                           providers=app.config['OPENID_PROVIDERS'])

