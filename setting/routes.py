# -*- coding:utf-8 -*-

from controller.common import MainHandler, HeartbeatHandler
from controller import auth
from controller import agent

urls = [
    (r"/", MainHandler),
    (r"/heartbeat", HeartbeatHandler),
    (r"/auth/login", auth.LoginHandler),
    (r"/agent/list", agent.ListHandler)
]