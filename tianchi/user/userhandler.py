#-*-coding=utf-8-*-

from tianchi.base.basehandler import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        print 'get LoginHandler'

class RegisterHandler(BaseHandler):
    def get(self):
        print 'get RegisterHandler'


