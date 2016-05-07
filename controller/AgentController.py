# -*- coding: utf-8 -*-

import tornado.web

from model import *

from dao.pattern import DataDaoFactory

from controller.base import BaseHandler


class ListHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(ListHandler, self).__init__(application, request, **kwargs)
        self.uap_dao = DataDaoFactory().get('UserAgentPermissionDao')

    @tornado.web.authenticated
    def get(self):
        agents = self.uap_dao.find_agents_by_user(self.current_user)
        get_permission = lambda agent: self.uap_dao.find_pemission(self.current_user, agent)
        self.render('agent/list.html', agents=agents, permission=get_permission)

class AddHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(AddHandler, self).__init__(application, request, **kwargs)
        self.agent_dao = DataDaoFactory().get('AgentDao')
        self.uap_dao = DataDaoFactory().get('UserAgentPermissionDao')

    def get(self):
        self.render('agent/add.html')

    def post(self):
        kvs = dict()
        for key in ('name', 'host', 'port'):
            kvs[key] = self.get_argument(key, '')
        agent = Agent(**kvs)
        agent.id = self.agent_dao.save(agent)
        uap = UserAgentPermission(user_id=self.current_user.id,
                                  agent_id=agent.id,
                                  permission_id=Permission.OWNER)
        self.uap_dao.save(uap)
        self.write(self.build_body(302, '/agent/list'))

class ManageHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(ManageHandler, self).__init__(application, request, **kwargs)
        # TODO

    def get(self, agent_name):
        self.render('agent/manage.html')

    def post(self):
        pass
