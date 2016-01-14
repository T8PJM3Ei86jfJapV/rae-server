# -*- coding: utf-8 -*-

import tornado.web

from model.base import *

from dao.base import *
from dao.pattern import DataDaoFactory

from controller.common import BaseHandler


class LoginHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(LoginHandler, self).__init__(application, request, **kwargs)
        self.user_dao = DataDaoFactory().get('UserDao')

    def get(self):
        self.render('login.html')

    def post(self):
        username, password = self.get_argument('username', ''), self.get_argument('password', '')
        user = self.user_dao.get_by_name(username) if self.user_dao.is_valid(User(username, password)) else None
        if user is not None:
            self.set_secure_cookie("user", str(user.id))
            self.redirect(self.get_argument("next", "/"))
        else:
            self.render("login.html", error="incorrect username or password")

class RegisterHandler(BaseHandler):
    def get(self):
        self.write('Hello Wolrd!')

    def post(self):
        pass