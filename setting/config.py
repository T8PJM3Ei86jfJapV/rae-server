# -*- coding:utf-8 -*-

from os import path

settings = { 
    "static_path": path.join(path.dirname(__file__), "..", "static"),
    "template_path": path.join(path.dirname(__file__), "..", "templates"),
    "login_url": "/auth/login",
    "cookie_secret": "Do63nua7TRa67R61dxxKYE4oxOkCJ06igBkbsPGtRzw=",
    "debug": True,
    "gzip": True,
}

mysql = {
    "host": "192.168.229.135:3306",
    "database": "hello",
    "user": "user",
    "password": "password",
}