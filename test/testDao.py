# -*- coding: utf-8 -*-

from dao.base import *
from model import *


def main():
    agent_dao = AgentDao()
    user_dao = UserDao()
    permission_dao = PermissionDao()
    user_agent_permission_dao = UserAgentPermissionDao()

    user = User(username=get_string(), password=get_string(), deleted=1)
    user_id = user_dao.save(user)
    user = user_dao.get_by_id(user_id)
    user.deleted = 0
    user.password += 'PSW'
    user_dao.save_or_update(user)
    print [(x.username, x.password) for x in user_dao.list()]

    permission = permission_dao.get_by_id(2)
    print permission.id, permission.name, permission.deleted

    user_agent_permission_dao.save(UserAgentPermission(user_id=1, agent_id=1, permission_id=1))
    user_agent_permission_dao.save(UserAgentPermission(user_id=1, agent_id=2, permission_id=2))
    user_agent_permission_dao.save(UserAgentPermission(user_id=1, agent_id=1, permission_id=2))
    print user_agent_permission_dao.find_agents_by_user(user_dao.get_by_id(1))[0].name
    print user_agent_permission_dao.find_pemissions(user_dao.get_by_id(1), agent_dao.get_by_id(1))[1].name
    user_agent_permission_dao.delete_by_id(3)
    print user_agent_permission_dao.find_pemissions(user_dao.get_by_id(1), agent_dao.get_by_id(1))[0].name


if __name__ == "__main__":
    main()
