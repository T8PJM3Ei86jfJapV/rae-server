# -*- coding: utf-8 -*-

import tornado.web

from model import *
from controller.base import BaseHandler

from dao.pattern import DataDaoFactory

from service import AgentService as agent_service


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

    def get(self, agent_id):
        try:
            agent = agent_service.get_agent_by_id(agent_id)
        except:
            self.build_body(403, 'Forbidden: agent not exists!')

        # get agent status
        try:
            alive = agent_service.alive(agent)
        except:
            alive = False
        status = 'Running' if alive else 'Stopped'

        # get rel_path of last package belongs to agent
        try:
            pkg = agent_service.get_last_package(agent.id)
        except:
            pkg = None
        finally:
            rel_path = '' if pkg is None else pkg.rel_path

        self.render('agent/manage.html',
                    agent=agent, status=status, rel_path=rel_path)

    def post(self):
        a_id = self.get_argument('agent_id', None)
        a_name = self.get_argument('agent_name', None)
        a_action = self.get_argument('agent_action', None)
        package_link = self.get_argument('package_link', None)

        # Any of a_id, a_name, a_action id None,
        # can not be None.
        if a_id and a_name and a_action is None:
            self.build_body(403, 'Parameters following are needed: agent_id, agent_name, agent_action')

        try:
            agent = agent_service.get_agent_by_id(a_id)
        except:
            raise Exception(500, 'Internal error when finding agent by id')

        if a_action == 'fetch':
            # if agent_action is 'fetch',
            # package_link can not be None.
            if package_link is None:
                self.build_body(403, 'Parameters following are needed: package_link')
            else:
                agent_service.fetch(agent, package_link)

        if a_action == 'start':
            agent_service.start(agent)

        if a_action == 'restart':
            agent_service.restart(agent)

        if a_action == 'stop':
            agent_service.stop(agent)

        if a_action == 'alive':
            # Check if service is running or not
            alive = agent_service.alive(agent)
            if alive:
                self.build_body(200, 'running')
            else:
                self.build_body(300, 'stopped')
