# -*- coding: utf-8 -*-

import tornado.web

from model import *

from dao.base import *
from dao.pattern import DataDaoFactory

from controller.common import BaseHandler


class LoginHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(LoginHandler, self).__init__(application, request, **kwargs)
        self.user_dao = DataDaoFactory().get('UserDao')

    def get(self):
        if self.get_current_user() is not None:
            self.redirect(self.get_argument('next', '/'))
        self.render('login.html')

    def post(self):
        username, password = self.get_argument('username', ''), self.get_argument('password', '')
        user = self.user_dao.get_by_name(username) if self.user_dao.is_valid(User(username, password)) else None
        if user is not None:
            self.set_secure_cookie("user", str(user.id))
            self.write(self.build_body(200))
        else:
            self.write(self.build_body(403, 'incorrect username or password'))


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect(self.get_argument('next', '/'))


class RegisterHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(RegisterHandler, self).__init__(application, request, **kwargs)
        self.user_dao = DataDaoFactory().get('UserDao')

    def get(self):
        if self.get_current_user() is not None:
            self.render('error.html')
        self.render('register/form.html')

    def post(self):
        username, password = self.get_argument('username', ''), self.get_argument('password', '')
        user = self.user_dao.get_by_name(username) if self.user_dao.is_valid(User(username, password)) else None
        if user is None:
            user.id = self.user_dao.save(user)
            self.set_secure_cookie("user", str(user.id))
            self.write(self.build_body(200))
        else:
            # The username is already exists.
            self.write(self.build_body(400, 'username is already exists'))