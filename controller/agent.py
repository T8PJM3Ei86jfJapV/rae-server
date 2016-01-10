# -*- coding: utf-8 -*-

import tornado.web

from dao.base import *


class ListHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")