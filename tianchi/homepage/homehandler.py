#-*-coding=utf-8-*-

from tianchi.base.basehandler import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        print 'get HomeHandler'

