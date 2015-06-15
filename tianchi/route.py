# -*- coding:utf8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import re
from tornado.web import Application

from tianchi.homepage.homehandler import HomeHandler
from tianchi.user.userhandler import (
    LoginHandler,
    RegisterHandler,
    )
from tianchi.restaurant.restauranthandler import RestaurantHandler
from tianchi.food.foodhandler import (
    FoodListHandler,
    FoodInfoHandler,
    )


def route():
    handlers = []
    handlers.append((r'/',HomeHandler))
    handlers.append((r'/login',LoginHandler))
    handlers.append((r'/register',RegisterHandler))
    handlers.append((r'/restaurant',RestaurantHandler))
    handlers.append((r'/foodlist',FoodListHandler))
    handlers.append((r'/foodinfo',FoodInfoHandler))
    return handlers

def settings():
    settings= dict(
        app_title       = 'Everyday to eat,everydata to come',
        templates_path  = os.path.join(os.path.dirname(__file__),'templates'),
        static_path     = os.path.join(os.path.dirname(__file__),'statics'),
        DEBUG           = True,
        gizp            = True,
        xsrf_cookies    = False,
        )
    return settings

handlers = route()
settings = settings()
App = Application(handlers,**settings)

if __name__== '__main__':
    app = route()
    print app.__dict__
