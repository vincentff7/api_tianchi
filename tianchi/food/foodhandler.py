#-*-coding=utf-8-*- 

from tianchi.base.basehandler import BaseHandler
from tianchi.food.foodquery import get_food_id_list_by_rstrnt_category
from tianchi.food.foodquery import  get_common_foods_by_food_ids 
#from tianchi.food.categoryquery import get_name_by_category_id
from tianchi.util.object_build import (
    build_component_common_food_list_item,
    build_component_food_list_item,
    )
from tianchi.food.food_rstrnt_query import get_foods_by_food_ids  
from tianchi.image.imagequery import get_img_url_by_img_id

class FoodHandler(BaseHandler):
    def get(self):
        '''
        返回店铺的实物列表
        '''
        rstrnt_id = self.get_argument('restaurant_id','1') 
        category_id = self.get_argument('category_id','1')
        offset = self.get_argument('offset','0')
        if not str(rstrnt_id).isdigit() or not str(category_id).isdigit() or not str(offset).isdigit():
            return '传输数据有误'

        food_ids = get_food_id_list_by_rstrnt_category(rstrnt_id,category_id,offset,limit = 20)
        foods = get_foods_by_food_ids(food_ids)
        base_foods = get_common_foods_by_food_ids(food_ids)
        res = []
        data = {}
        for item in base_foods:
            base_com_= build_component_common_food_list_item(item)
            data[base_com['id']] = base_com
        for item in foods:
            com = build_component_food_list_item(item)
            if com['id'] in data.keys():
                data[com['id']].update(com['id'])
                res.append(data[com['id']])
            else:
                pass
        return res



