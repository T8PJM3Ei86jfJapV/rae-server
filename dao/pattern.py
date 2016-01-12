# -*- coding: utf-8 -*-

from dao.base import *
from dao.data import *


class DataDaoFactory(Singleton):
    def get(self, kls):
        kls = 'dao.data.%s' % kls
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m()