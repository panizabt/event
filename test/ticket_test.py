from model.entity import *
from model.service.ticket_service import TicketService
from controller.ticket_controller import TicketController

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from model.entity.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


start_date = datetime(2024, 11, 12, 20, 17, 30)
# ticket = Ticket(None, "title", start_date, 15, None, 10000, None, None)

TicketController.save("concert", start_date, 90, "concert music", 1000000, "Credit Card", 111)
