# -*- coding:utf-8 -*-


class Agent(object):
    def __init__(self, host, port, id=0, name='', enable=1, deleted=0):
        self.id = id
        self.name = name
        self.host = host
        self.port = port
        self.enable = enable
        self.deleted = deleted


class User(object):
    def __init__(self, username, password, id=0, deleted=0):
        self.id = id
        self.username = username
        self.password = password
        self.deleted = deleted


class Permission(object):
    READ = 1
    WRITE = 2
    def __init__(self, name, id=0, deleted=0):
        self.id = id
        self.name = name
        self.deleted = deleted


class UserAgentPermission(object):
    def __init__(self, user_id, agent_id, permission_id, id=0, deleted=0):
        self.id = id
        self.user_id = user_id
        self.agent_id = agent_id
        self.permission_id = permission_id
        self.deleted = deleted
