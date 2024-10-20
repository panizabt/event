from controller.salon_controller import SalonController
from model.entity import *

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists



connection = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection):
    create_database(connection)

engine=create_engine(connection)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


SalonController.save(1,"aria","teh",300,"fgded",True)
SalonController.edit()