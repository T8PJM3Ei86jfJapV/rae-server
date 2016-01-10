# -*- coding: utf-8 -*-

import tornado.web

from dao.base import *


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username, password = self.get_argument("username"), self.get_argument("password")
        self.write("%s, %s" % (username, password))


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Wolrd!")

    def post(self):
        pass