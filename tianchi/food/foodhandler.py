#-*-coding=utf-8-*- 

from tianchi.base.basehandler import BaseHandler
from tianchi.food.food_rstrnt_query import get_food_id_list_by_rstrnt_category
from tianchi.food.foodquery import  (
    get_common_foods_by_food_ids,
    get_common_food_by_food_id,
    )
#from tianchi.food.categoryquery import get_name_by_category_id
from tianchi.util.object_build import (
    build_component_common_food_list_item,
    build_component_food_list_item,
    build_component_common_food_info_item,
    build_component_food_info_item,
    )
from tianchi.food.food_rstrnt_query import (
    get_foods_by_food_ids,
    get_food_by_food_id,
    )

class FoodListHandler(BaseHandler):
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
            base_com= build_component_common_food_list_item(item)
            print base_com
            data[base_com['component']['id']] = base_com
        for item in foods:
            com = build_component_food_list_item(item)
            if com['component']['id'] in data.keys():
                data[com['component']['id']].update(com)
                res.append(data[com['component']['id']])
            else:
                pass
        return res

class FoodInfoHandler(BaseHandler):
    def get(self):
        rstrnt_id = self.get_argument('restaurant_id','')
        category_id = self.get_argument('category_id','')
        food_id =  self.get_argument('food_id','')
        if not str(rstrnt_id).isdigit() or not str(category_id).isdigit() or not str(food_id).isdigit():
            return '传输数据有误'
        com = {}
        base_food = get_common_food_by_food_id(food_id)
        com_food_info = build_component_common_food_info_item(base_food)
        food = get_food_by_food_id(food_id,rstrnt_id,category_id)
        food_info = build_component_food_info_item(food)
        if com_food_info['food_id'] == food_info['food_id']:
            com = com_food_info.update(food_info)
        return com



