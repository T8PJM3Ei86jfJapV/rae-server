# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options

from setting.routes import urls
from setting.config import settings
from setting.config import site

from tornado.options import define, options
define("port", default=site.get('port', 8080), help="run on the given port", type=int)

def run(port):
    application = tornado.web.Application(urls, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    run(options.port)