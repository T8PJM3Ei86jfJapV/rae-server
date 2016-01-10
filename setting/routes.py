# -*- coding:utf-8 -*-

from controller.common import *
from controller import auth

urls = [
    (r"/", MainHandler),
    (r"/heartbeat", HeartbeatHandler),
    (r"/auth/login", auth.LoginHandler)
]