# -*- coding:utf-8 -*-


class Singleton(object):
    """ Singleton Base Class
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Maybe(object):
    def __init__(self):
        self.name = '233'


class DaoFactory(Singleton):
    def get(self, kls):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m


if __name__ == "__main__":
    fac = DaoFactory()
    dao = fac.get('Maybe')
    print type(dao), dao.name