# -*- coding:utf-8 -*-

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")


class HeartbeatHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")