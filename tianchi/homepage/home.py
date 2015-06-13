#-*-coding=utf-8-*-

from tianchi.handler.basehandler import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        print 'get HomeHandler'

