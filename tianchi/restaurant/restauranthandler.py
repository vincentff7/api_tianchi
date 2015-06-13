#-*-coding=utf-8-*-

from tianchi.base.basehandler import BaseHandler

class RestaurantHandler(BaseHandler):
    def get(self):
        print 'get RestaurantHandler'
