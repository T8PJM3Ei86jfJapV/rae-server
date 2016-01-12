# -*- coding: utf-8 -*-

from dao.base import *
from model.base import *


class AgentDao(BaseDao):
    """ Agent DAO Class
    """
    def __init__(self):
        super(AgentDao, self).__init__()

    def get_by_id(self, id):
        """Get an agent object by id.

        id -- integer

        Note: If the query has no results, returns None. If it has
        more than one result, raises an exception.
        """
        sql = 'select * from agent where deleted = 0 and id = %(id)s'
        res = self.db.get(sql, id=id)
        return Agent(**res) if res is not None else None

    def delete_by_id(self, id):
        """Delete an agent object by id.

        id -- integer
        """
        sql = 'update agent set deleted = 1 where id = %(id)s'
        self.db.execute(sql, id=id)

    def list(self, start=0, limit=100):
        """Get all of agent objects.

        start -- integer, begin id of agent, 0 in default
        limit -- integer, size limit of result, 100 in default

        Returns a list of agent.
        Note: If the query has no results, returns an empty list.
        """
        sql = 'select * from agent where deleted = 0 limit %(start)s, %(limit)s'
        return [Agent(**x) for x in self.db.query(sql, start=start, limit=limit)]

    def save(self, agent):
        """Insert an agent object into database

        agent -- Agent

        Returns id of agent inserted.
        """
        sql = 'insert into agent(name, host, port) ' \
              'values(%(name)s, %(host)s, %(port)s) '
        return self.db.execute(sql, name=agent.name, host=agent.host, port=agent.port)

    def update(self, agent):
        """Update an agent object into database by its id

        agent -- Agent

        Returns 0.
        """
        sql = 'update agent set name = %(name)s, host = %(host)s, port = %(port)s, ' \
              'enable = %(enable)s, deleted = %(deleted)s where id = %(id)s'
        return self.db.execute(sql, id=agent.id, name=agent.name, host=agent.host,
                               port=agent.port, enable=agent.enable, deleted=agent.deleted)

    def save_or_update(self, agent):
        """Save or update an agent object into database by its id

        agent -- Agent

        Note:
            If the id of agent equals to 0, save it into database. If the id
        is not equals to 0, update by its id.
            If save successfully, returns the id of agent inserted. If update
        successfully or not, return 0.
        """
        return self.save(agent) if agent.id == 0 else self.update(agent)


class UserDao(BaseDao):
    """ User DAO Class
    """
    def __init__(self):
        super(UserDao, self).__init__()

    def get_by_id(self, id):
        """Get an user object by id.

        id -- integer, id of user

        Note: If the query has no results, returns None. If it has
        more than one result, raises an exception.
        """
        sql = 'select * from sys_user where deleted = 0 and id = %(id)s'
        res = self.db.get(sql, id=id)
        return User(**res) if res is not None else None

    def get_by_name(self, username):
        """Get an user object by username.

        username -- string, username of user

        Note: If the query has no results, returns None. If it has
        more than one result, raises an exception.
        """
        sql = 'select * from sys_user where deleted = 0 and username = %(username)s'
        res = self.db.get(sql, username=username)
        return User(**res) if res is not None else None

    def delete_by_id(self, id):
        """Delete a user object by id.

        id -- integer
        """
        sql = 'update sys_user set deleted = 1 where id = %(id)s'
        self.db.execute(sql, id=id)

    def list(self, start=0, limit=100):
        """Get all of user objects.

        start -- integer, begin id of sys_user, 0 in default
        limit -- integer, size limit of result, 100 in default

        Returns a list of user.
        Note: If the query has no results, returns an empty list.
        """
        sql = 'select * from sys_user where deleted = 0 limit %(start)s, %(limit)s'
        return [User(**x) for x in self.db.query(sql, start=start, limit=limit)]

    def save(self, user):
        """Insert a user object into database.

        user -- User

        Returns id of user inserted.
        """
        sql = 'insert into sys_user(username, password) ' \
              'values(%(username)s, %(password)s) '
        return self.db.execute(sql, username=user.username, password=user.password)

    def update(self, user):
        """Update an user object into database by its id.

        user -- User

        Returns 0.
        """
        sql = 'update sys_user set username = %(username)s, password = %(password)s, ' \
              'deleted = %(deleted)s where id = %(id)s'
        return self.db.execute(sql, id=user.id, username=user.username, password=user.password,
                               deleted=user.deleted)

    def save_or_update(self, user):
        """Save or update a user object into database by its id.

        user -- User

        Note:
            If the id of user equals to 0, save it into database. If the id
        is not equals to 0, update by its id.
            If save successfully, returns the id of user inserted. If update
        successfully or not, return 0.
        """
        return self.save(user) if user.id == 0 else self.update(user)

    def is_valid(self, user):
        """Check if an user is valid.

        user -- User

        Note: If the username and password are valid, return True. Return False otherwise.
        """
        sql = 'select count(1) as count from sys_user where deleted = 0 ' \
              'and username = %(username)s and password = %(password)s'
        return self.db.query(sql, username=user.username, password=user.password).count != 0


class PermissionDao(BaseDao):
    """ Permission DAO Class
    """
    def __init__(self):
        super(PermissionDao, self).__init__()

    def get_by_id(self, id):
        sql = 'select * from permission where deleted = 0 and id = %(id)s'
        res = self.db.get(sql, id=id)
        return Permission(**res) if res is not None else None


class UserAgentPermissionDao(BaseDao):
    def __init__(self):
        super(UserAgentPermissionDao, self).__init__()

    def save(self, user_agent_permission):
        sql = 'insert into user_agent_permission(user_id, agent_id, permission_id) ' \
              'values(%(user_id)s, %(agent_id)s, %(permission_id)s)'
        return self.db.execute(sql, user_id=user_agent_permission.user_id, agent_id=user_agent_permission.agent_id,
                               permission_id=user_agent_permission.permission_id)

    def delete_by_id(self, id):
        sql = 'update user_agent_permission set deleted = 1 where id = %(id)s'
        self.db.execute(sql, id=id)

    def find_agents_by_user(self, user):
        sql = 'select * from agent where exists ( ' \
              'select distinct (t.agent_id) from user_agent_permission t ' \
              'join agent a on t.agent_id = a.id where t.deleted = 0  and t.user_id = %(user_id)s' \
              ') and deleted = 0;'
        return [Agent(**x) for x in self.db.query(sql, user_id=user.id)]

    def find_pemissions(self, user, agent):
        sql = 'select p.* from user_agent_permission t ' \
              'join permission p on t.permission_id = p.id ' \
              'where t.user_id = %(user_id)s and t.agent_id = %(agent_id)s ' \
              'and t.deleted = 0 and p.deleted=0'
        return [Permission(**x) for x in self.db.query(sql, user_id=user.id, agent_id=agent.id)]


import random, string
def get_string():
    return ''.join([random.choice(string.ascii_letters) for _ in range(6)])

if __name__ == "__main__":
    agent_dao = AgentDao()
    user_dao = UserDao()
    permission_dao = PermissionDao()
    user_agent_permission_dao = UserAgentPermissionDao()

    # user = User(username=get_string(), password=get_string(), deleted=1)
    # user_id = user_dao.save(user)
    # user = user_dao.get_by_id(user_id)
    # user.deleted = 0
    # user.password += 'PSW'
    # user_dao.save_or_update(user)
    # print [(x.username, x.password) for x in user_dao.list()]

    # permission = permission_dao.get_by_id(2)
    # print permission.id, permission.name, permission.deleted

    # user_agent_permission_dao.save(UserAgentPermission(user_id=1, agent_id=1, permission_id=1))
    # user_agent_permission_dao.save(UserAgentPermission(user_id=1, agent_id=2, permission_id=2))
    # user_agent_permission_dao.save(UserAgentPermission(user_id=1, agent_id=1, permission_id=2))
    # print user_agent_permission_dao.find_agents_by_user(user_dao.get_by_id(1))[0].name
    # print user_agent_permission_dao.find_pemissions(user_dao.get_by_id(1), agent_dao.get_by_id(1))[1].name
    # user_agent_permission_dao.delete_by_id(3)
    # print user_agent_permission_dao.find_pemissions(user_dao.get_by_id(1), agent_dao.get_by_id(1))[0].name
