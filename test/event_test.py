from controller.event_controller import EventController
from model.entity.event import Event
from model.service.event_service import EventService

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from model.entity.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

d_t = datetime(2024,5,23,18, 0, 0)
s_t = datetime(2024,5,23,18,0,0)
e_t = datetime(2024,5,23,20,0,0)
EventController.save(d_t, s_t, e_t, "konsert", 120, "lotfan 2 saat zod tar hozor peyda konid", 650000)
EventController.save(d_t, s_t, e_t, "film", 90, "lotfan 2 saat zod tar hozor peyda konid", 80000 )
