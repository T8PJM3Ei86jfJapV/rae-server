# -*- coding: utf-8 -*-

import tornado.web

from dao.pattern import DataDaoFactory

from controller.common import BaseHandler


class ListHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(ListHandler, self).__init__(application, request, **kwargs)
        self.agent_dao = DataDaoFactory().get('AgentDao')

    @tornado.web.authenticated
    def get(self):
        agents =  self.agent_dao.list()
        self.write("Hello World!")