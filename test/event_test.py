from controller.event_controller import EventController
from datetime import datetime
from time import time
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from model.entity.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

d_t = datetime(2024,5,23,None,None,None)
s_t = time
e_t = datetime(None,None,None,20,0,0)
print (EventController.save( d_t, s_t, e_t,"konserr", "konsert ziba" "2000"
print (EventController.edit(None
print (EventController.remove(
