# -*- coding:utf-8 -*-

from controller.common import MainHandler, HeartbeatHandler
from controller import auth
from controller import agent

urls = [
    (r"/", MainHandler),
    (r"/heartbeat", HeartbeatHandler),
    (r"/auth/login", auth.LoginHandler),
    (r"/auth/logout", auth.LogoutHandler),
    (r"/auth/register", auth.RegisterHandler),
    (r"/agent/add", agent.AddHandler),
    (r"/agent/list", agent.ListHandler)
]