# -*- coding:utf-8 -*-

import time


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
    FORBID = 1
    VISITOR = 2
    ADMIN = 3
    OWNER = 4
    def __init__(self, name, id=1, deleted=0):
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


class Package(object):
    def __init__(self, filename, id=0, create_time=time.strftime('%Y-%m-%d %H:%M:%S'), deleted=0):
        self.id = id
        self.filename = filename
        self.create_time = create_time
        self.deleted = deleted


class Service(object):
    def __init__(self, agent_id, package_id, id=0, deleted=0):
        self.id = id
        self.agent_id = agent_id
        self.package_id = package_id
        self.deleted = deleted


def main():
    permission = Permission(None)
    print permission.id, permission.name, permission.deleted

if __name__ == "__main__":
    main()