#-*-coding=utf-8-*-

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

class Category(Base,BaseComponent):
    __tablename__ = 'tc_categorys'
    category_id = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(VARCHAR,nullable = True,default = '')
    review = Column(TINYINT,nullable = False)
    recommend = Column(TINYINT,nullable = True,default = 1)

def get_name_by_category_id(category_id):
    DBsession = dbsession_generator()
    res_name = DBsession.query(Category.name).filter(Category.category_id ==int(category_id)).filter(Category.review == 1).first()
    DBsession.close()
    return res_name[0] if res_name else ''

if __name__ == '__main__':
    name = get_name_by_category_id(2)
    print name
