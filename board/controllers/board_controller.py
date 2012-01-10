#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from board import db
from board.models.entry import Entry
from board.models.user import User
from board.controllers.forms import EntryForm, LoginForm, CreateUserForm

app = Blueprint('board', __name__)

@app.route('/')
def index():
    entries = Entry.query.order_by(db.desc('created_date')).all()
    return render_template('index.html', entries=entries)

@app.route('/user/add', methods=['POST', 'GET'])
def add_user():
    error = None
    form = CreateUserForm()
    if form.validate_on_submit():
        user = User(username=request.form['username'], password=request.form['password'])
        try:
            user.save()
        except Exception, e:
            error = u"そのユーザ名は登録できません"
        else:
            flash(u"登録が完了しました")
            return redirect(url_for('.index'))

    elif form.is_submitted() and not error:
        error = u"入力値が正しくありません"
    return render_template('add_user.html', form=form, error=error)

@app.route('/entry/add', methods=['POST', 'GET'])
def add_entry():
    form = EntryForm()
    error = None

    if not 'user' in session:
        abort(403)

    if form.validate_on_submit():
        entry = Entry(title=request.form['title'], text=request.form['text'], user_id=session['user'].id)
        entry.save()
        flash(u"投稿しました")
        return redirect(url_for('.index'))

    if form.is_submitted():
        error = u"入力値が正しくありません"
    return render_template('add_entry.html', form=form, error=error)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter(User.username==username).first()
    print user
    if user and user.check_password(password):
        session['user'] = user
        flash(u"ログイン完了しました")
    else:
        flash(u"ログイン失敗しました")

    return redirect(url_for('.index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash(u"ログアウトしました")
    return redirect(url_for('.index'))

@app.errorhandler(403)
def forbidden(e):
    return render_template('error/403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

@app.teardown_request
def teardown_request(exception):
    pass
