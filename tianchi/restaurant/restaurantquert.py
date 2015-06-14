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

class Restaurant(Base,BaseComponent):
    __tablename__ = 'tc_food_rstrnts'
    rstrnt_id = Column(INTEGER, primary_key = True, autoincrement = True)
    rstrntname = Column(VARCHAR(32),nullable = True,default = "")
    types = Column(TINYINT,nullable = True,default = 1)
    address = Column(VARCHAR(128),nullable = True ,default = '')
    logo = Column(VARCHAR(128),nullable = True,default = '')
    two_dim_code =  Column(VARCHAR(128), nullable = True,default = '')
    email = Column(VARCHAR(128),nullable=True,default = 'example@email.com')
    mobile_num = Column(VARCHAR(16),nullable = True)



    def get_component_id(self):
        return str(self.rstrnt_id)

    def get_component_rstrntname(self):
        return self.rstrntname

    def get_component_rstrnt_address(self):
        return self.address

    def get_component_logo(self):
        return self.logo

    def get_component_twodimcode(self):
        return self.two_dim_code

    def get_component_email(self):
        return self.email

    def get_component_mobile_num(self):
        return self.mobile_num







