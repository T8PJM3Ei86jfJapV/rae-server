# -*- coding:utf-8 -*-

import tornado.web

from dao.pattern import DataDaoFactory


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.user_dao = DataDaoFactory().get('UserDao')

    def get_current_user(self):
        user_id = self.get_secure_cookie('user')
        if not user_id: return None
        return self.user_dao.get_by_id(int(user_id))


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello World!")


class HeartbeatHandler(BaseHandler):
    def get(self):
        self.write("Hello World!")