#-*-coding=utf-8-*-

from sqlalchemy import (
    Column,
    INTEGER,
    VARCHAR,
    BIGINT,
    DECIMAL
    )
from sqlalchemy.dialects.mysql import TINYINT
from tianchi.config.db import (
    Base,
    dbsession_generator,
    )
from tianchi.base.base_component import BaseComponent
from tianchi.image.imagequery import get_img_url_by_img_id

class FoodRstrnt(Base,BaseComponent):
    __tablename__ = 'tc_food_rstrnts'
    id = Column(INTEGER, primary_key = True, autoincrement = True)
    food_id = Column(INTEGER,nullable =  False)
    rstrnt_id = Column(INTEGER,nullable = False)
    category_id = Column(INTEGER,nullable = False)
    original_price = Column(DECIMAL(7, 2, asdecimal = False), nullable = False, default = 0)
    discount = Column(DECIMAL(6, 2, asdecimal = False), nullable = False, default = 1) # 折扣，存的小数，可以直接乘以原价得到折扣价。
    img_ids = Column(VARCHAR(64),nullable = False)
    food_desc = Column(VARCHAR(256))
    ispepery = Column(TINYINT,nullable = False)
    types = Column(TINYINT,nullable = False)
    category_id = Column(INTEGER,nullable = True,default = 1)
    
    def get_component_food_id(self):
        return str(self.food_id)

    def get_component_rstrnt_id(self):
        return str(self.rstrnt_id)

    def get_component_category_id(self):
        return str(self.category_id)

    def get_component_price(self):
        if self.discount:
            price = self.original_price * self.discount
        return str(price)

    def get_component_pic_url(self):
        img_ids = str(self.img_ids)
        img_id_list = img_ids.split(',')
        pic_url_list = []
        for img_id in img_id_list:
            url = {}
            pic_url = get_img_url_by_img_id(img_id)
            url[img_id] = pic_url
            pic_url_list.append(url)
        return pic_url_list

    def get_component_original_price(self):
        return str(self.original_price)

    def get_component_desc(self):
        return self.food_desc

    def get_component_ispepery(self):
        return self.ispepery

    def to_ui_action(self):
        return None


  
def get_food_id_list_by_rstrnt_category(rstrnt_id,category_id):
    DBsession = dbsession_generator()
    res_ids = DBsession.query(FoodRstrnt.id).filter(
        FoodRstrnt.rstrnt_id == int(rstrnt_id)).filter(
        FoodRstrnt.category_id == int(category_id )).all()
    DBsession.close()
    ids = [id[0] for id in res_ids]
    return ids

def get_foods_by_food_ids(food_ids):
    DBsession = dbsession_generator()
    foods = DBsession.query(FoodRstrnt).filter(
        FoodRstrnt.food_id.in_(food_ids)).all()
    DBsession.close()
    return foods

def get_food_by_food_id(food_id,rstrnt_id,category_id):
    DBsession = dbsession_generator()
    food = DBsession.query(FoodRstrnt).filter(
        FoodRstrnt.food_id == int(food_id)).filter(
        FoodRstrnt.rstrnt_id == int(rstrnt_id)).filter(
        FoodRstrnt.category_id == int(category_id)).first()
    DBsession.close()
    return food 

if __name__ == "__main__":
    ids = get_food_id_list_by_rstrnt_category(1,3)
    print ids
    foods = get_foods_by_food_ids(ids)
    for food in foods:
        print food.get_component_desc()
        print food.get_component_original_price()
