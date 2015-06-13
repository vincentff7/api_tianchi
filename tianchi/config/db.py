# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
        scoped_session,
        sessionmaker,    
    )
from zope.sqlalchemy import ZopeTransactionExtension

MYSQL_USER = 'api'
MYSQL_HOST = 'localhost'
MYSQL_PASSWD = 'shushanbj'
MYSQL_PORT = '3306'
MYSQL_DBNAME = 'tainchi'

SQLALCHEMY_CONF_URL= 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8mb4' % (MYSQL_USER, MYSQL_PASSWD, MYSQL_HOST, MYSQL_PORT, MYSQL_DBNAME)

Base = declarative_base() 
engine = create_engine(SQLALCHEMY_CONF_URL, pool_recycle = 60)
DBSession = scoped_session(sessionmaker(extension = ZopeTransactionExtension(), bind = engine))

def dbsession_generator():
    return DBSession()

