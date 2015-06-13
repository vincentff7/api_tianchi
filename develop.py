# -*- coding:utf8 -*-

from tornado.ioloop import IOLoop
from zmq.eventloop import ioloop
from tornado import httpserver
import tornado.options
from tianchi.route import App

from tornado.options import (
    define,
    options,
    )

define("port",default=8899, help="run on the given port", type =int)

def start(port):
    http_server = httpserver.HTTPServer(App, xheaders=True)
    http_server.listen(port)
    ioloop.install()
    IOLoop.instance().start()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    start(options.port)

