# -*- coding: utf-8 -*-

from flaskext.wtf import Form, TextField, TextAreaField, PasswordField, validators

class EntryForm(Form):
    title = TextField('title', [validators.required(), validators.Length(max=255)])
    text = TextAreaField('text', [validators.required()])

class LoginForm(Form):
    username = TextField('username', [validators.required()])
    password = PasswordField('password', [validators.required()])

class CreateUserForm(Form):
    username = TextField('username', [validators.required()])
    password = PasswordField('password', [validators.required()])
    repassword = PasswordField('repassword', [
        validators.required(),
        validators.EqualTo('password', message=u"パスワードが一致しません")
    ])


