# -*- coding:utf-8 -*-

def build_component_food_list_item(obj):
    ui = {}
    if obj:
        ui['width'] = obj.get_component_width()
        ui['height'] = obj.get_component_height()
        com = {}
        com['componentType'] = 'item'
        com['id'] = obj.get_component_food_id()
        if obj.get_component_pic_url():
            com['picUrl'] = obj.get_component_pic_url()
        com['price'] = obj.get_component_price()
        com['original_price'] = obj.get_component_original_price()
        if obj.get_component_desc():
            com['description'] = obj.get_component_desc()
        if obj.get_component_ispepery():
            com['ispepery'] = obj.get_component_ispepery()
        com['action'] = obj.to_ui_action()
        ui['component'] = com
    return ui

def build_component_common_food_list_item(obj):
    ui = {}
    if obj:
        com = {}
        com['componentType'] = 'item'
        com['id'] = obj.get_component_id()
        com['name'] = obj.get_component_name()
        com['picUrl'] = obj.get_component_pic_url()
        com['description'] = obj.get_component_desc()
        com['ispepery'] = obj.get_component_ispepery()
        com['action'] = obj.to_ui_action()
        ui['component'] = com
    return ui

def build_component_common_food_info_item(obj):
    ui = {}
    if obj:
        com = {}
        com['componentType'] = 'info'
        com['id'] = obj.get_component_id()
        com['picUrl'] = obj.get_component_pic_url()
        com['name'] = obj.get_component_name()
        com['description'] = obj.get_component_desc()
        com['ispepery'] = obj.get_component_ispepery()
        ui['component'] = com
        return ui

def build_component_food_info_item(obj):
    ui = {}
    if obj:
        ui['width'] = obj.get_component_width()
        ui['height'] = obj.get_component_height()
        com = {}
        com['componentType'] = 'info'
        com['id'] = obj.get_component_food_id()
        if  obj.get_component_pic_url():
            com['picUrl'] = obj.get_component_pic_url()
        com['price'] = obj.get_component_price()
        com['original_price'] = obj.get_component_discount()
        if obj.get_component_desc():
            com['description'] = obj.get_component_desc()
        if obj.get_component_ispepery():
            com['ispepery'] = obj.get_component_ispepery()
        ui['component'] = com
    return ui
