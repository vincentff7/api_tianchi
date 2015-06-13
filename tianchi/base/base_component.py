#-*-coding=utf-8-*- 

class BaseComponent(object):
    def __init__(self):
        pass

    def get_component_id(self):
        raise Exception('Object is NOT available.')

    def get_component_img_url(self):
        raise Exception('object is NOT available.')

    def get_component_desc(self):
        raise Exception('object is NOT available.')
    
    def get_component_price(self):
        raise Exception('object is NOT available.')

    def get_component_year(self):
        raise Exception('object is NOT available.')

    def get_component_month(self):
        raise Exception('object is NOT available.')

    def get_component_day(self):
        raise Exception('object is NOT available.')

    def get_component_time(self):
        raise Exception('object is NOT available.')

    def get_component_width(self):
        return 100

    def get_component_height(self):
        return 100

    def get_component_user_name(self):
        raise Exception('object is NOT available.')

    def get_component_ispepery(self):
        raise Exception('object is NOT available.')

    def to_ui_action(self):
        raise Exception('object is NOT available.')
