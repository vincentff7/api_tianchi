# -*- coding:utf-8 -*-

from sqlalchemy import (
    Column,
    INTEGER,
    VARCHAR,
    BIGINT,
    )
from sqlalchemy.dialects.mysql import TINYINT
from tianchi.config.db import (
    Base,
    dbsession_generator,
    )
from tianchi.base.base_component import BaseComponent
from tianchi.image.imagequery import get_img_url_by_img_id

class Food(Base,BaseComponent):
    __tablename__ = 'tc_foods'
    food_id = Column(INTEGER, primary_key = True, autoincrement = True)
    food_name = Column(INTEGER, nullable = True,default = '')
    food_img_id = Column(INTEGER, nullable = True,default = 1)
    review =  Column(TINYINT, nullable = True,default = 1)
    types =  Column(INTEGER, nullable = True,default = 1)
    description = Column(VARCHAR,nullable = False)
    ispepery =  Column(INTEGER, nullable = True,default = 0)

    def get_component_id(self):
        return str(self.food_id)

    def get_component_name(self):
        return self.food_name

    def get_component_pic_url(self):
        url_list = []
        url = {}
        img_id =str(self.food_img_id())
        url[str(img_id)] = get_img_url_by_img_id(img_id)
        url_list.append(url)
        return url_list

    def get_component_desc(self):
        return self.description

    def get_component_ispepery(self):
        return str(self.ispepery)
    
    def to_ui_action(self):
        return None

def get_common_foods_by_food_ids(food_ids):
    DBSession = dbsession_generator()
    res = DBSession.query(Food).filter(
        Food.food_id.in_(food_ids)).filter(
        Food.review == 1).all()
    DBSession.close()
    return res

if __name__ =='__main__':
    food_ids = [1,2,3]
    foods = get_common_foods_by_food_ids(food_ids)
    if foods:
        print len(foods)
    else:
        print 'No food'
