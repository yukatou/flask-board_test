#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Module, render_template, request, redirect, url_for, flash, session
from board import db
from board.models.entry import Entry
from board.models.user import User
from board.controllers.forms import EntryForm, LoginForm, CreateUserForm

board = Module(__name__)

@board.route('/')
def index():
    entries = Entry.query.order_by(db.desc('created_date')).all()

    return render_template('index.html', entries=entries)

@board.route('/user/add', methods=['POST', 'GET'])
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
    return render_template('add_user.html', form=form, error=error)

@board.route('/entry/add', methods=['POST', 'GET'])
def add_entry():
    form = EntryForm()
    error = None

    if form.validate_on_submit():
        entry = Entry(title=request.form['title'], text=request.form['text'], user_id=session['logged_in'])
        entry.save()
        flash(u"投稿しました")
        return redirect(url_for('index'))

    if form.is_submitted():
        error = u"入力値が正しくありません"
    return render_template('add_entry.html', form=form, error=error)

@board.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        session['logged_in'] = user.id
        flash(u"ログイン完了しました")
    else:
        flash(u"ログイン失敗しました")

    return redirect(url_for('index'))

@board.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash(u"ログアウトしました")
    return redirect(url_for('index'))
