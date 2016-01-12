# -*- coding: utf-8 -*-

import tornado.web

from dao.base import *
from dao.pattern import *


class LoginHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(LoginHandler, self).__init__(application, request, **kwargs)
        self.user_dao = DataDaoFactory().get('UserDao')

    def get(self):
        self.render('login.html')

    def post(self):
        username, password = self.get_argument('username', ''), self.get_argument('password', '')
        user = self.user_dao.get_by_name(username) if self.user_dao.is_valid(User(username, password)) else None
        info = user.username if user is not None else 'None'
        self.write('Hello, %s' % info)


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello Wolrd!')

    def post(self):
        pass