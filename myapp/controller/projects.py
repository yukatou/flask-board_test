#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Module, render_template, request, redirect, url_for, flash, session
from myapp.model.projects import Entry, User
from myapp.controller.forms import EntryForm, LoginForm, CreateUserForm

projects = Module(__name__)

@projects.route('/')
def index():
 #   entriey = Entry.query.order_by(db.desc('created_date')).all()
    entries = Entry.query.order_by('created_date').all()

    return render_template('projects/index.html', entries=entries)

@projects.route('/user/add', methods=['POST', 'GET'])
def add_user():
    error = None
    form = CreateUserForm()
    if form.validate_on_submit():
        user = User(username=request.form['username'], password=request.form['password'])
        user.save()
        flash(u"登録が完了しました")
        return redirect(url_for('index'))

    if form.is_submitted():
        error = u"入力値が正しくありません"
    return render_template('projects/add_user.html', form=form, error=error)

@projects.route('/entry/add', methods=['POST', 'GET'])
def add_entry():
    form = EntryForm()
    error = None

    if form.validate_on_submit():
        entry = Entry(title=request.form['title'], text=request.form['text'])
        entry.save()
        flash(u"投稿しました")
        return redirect(url_for('index'))

    if form.is_submitted():
        error = u"入力値が正しくありません"
    return render_template('projects/add_entry.html', form=form, error=error)

@projects.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        session['logged_in'] = True
        flash(u"ログイン完了しました")
    else:
        flash(u"ログイン失敗しました")

    return redirect(url_for('index'))

@projects.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash(u"ログアウトしました")
    return redirect(url_for('index'))
