# -*- coding: utf-8 -*-

import tornado.web

from model.base import *

from dao.pattern import DataDaoFactory

from controller.common import BaseHandler


class ListHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(ListHandler, self).__init__(application, request, **kwargs)
        self.uap_dao = DataDaoFactory().get('UserAgentPermissionDao')

    @tornado.web.authenticated
    def get(self):
        agents = self.uap_dao.find_agents_by_user(self.get_current_user())
        self.write(''.join((agent.name for agent in agents)))

class AddHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(AddHandler, self).__init__(application, request, **kwargs)
        self.agent_dao = DataDaoFactory().get('AgentDao')

    def get(self):
        self.render('agent/add.html')

    def post(self):
        kvs = dict()
        for key in ('name', 'host', 'port'):
            kvs[key] = self.get_argument(key, '')
        agent = Agent(**kvs)
        self.agent_dao.save(agent)
        # add a record into user_agent_permission here
        self.write(self.build_body(200))

class AdminHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(AdminHandler, self).__init__(application, request, **kwargs)
        # TODO

    def get(self):
        self.render('agent/admin.html')

    def post(self):
        pass
