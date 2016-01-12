# -*- coding: utf-8 -*-

from torndb import Connection

from setting.config import mysql


class Singleton(object):
    """ Singleton Base Class
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class BaseDao(Singleton):
    """ Base DAO Class
    """
    def __init__(self):
        self.db = Connection(**mysql)


