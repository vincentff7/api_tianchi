#-*-coding=utf-8-*-

import re
from sqlalchemy import(
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

PREFIX = r'/home/quwm/workspace/api_tianchi/tianchi/statics/images/'

class Image(Base,BaseComponent):
    __tablename__ = 'tc_image'
    image_id = Column(INTEGER, primary_key = True, autoincrement = True)
    url = Column(VARCHAR(128),nullable = False)
    height = Column(INTEGER(8),nullable = True, default = 0)
    width  = Column(INTEGER(8),nullable = True,default = 0)
    review = Column(TINYINT,nullable = True,default = 1)
    namespace = Column(VARCHAR(32),nullable = False)
    types = Column(TINYINT,nullable = True,default = 1)

    def get_component_id(self):
        return str(self.image_id)

    def get_component_url(self):
        url = str(self.url)
        return PREFIX+url

    def get_component_height(self):
        return self.height

    def get_component_wight(self):
        return self.wight


def get_img_url_by_img_id(img_id):
    DBsession = dbsession_generator()
    url = DBsession.query(Image.url).filter(
        Image.img_id == int(img_id)).filter(
        Image.review ==1).first()
    DBsession.close()
    return url

