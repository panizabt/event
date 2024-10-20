from controller.salon_controller import SalonController

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from model.entity.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


SalonController.save(1,"amir","tehran",300,"gfsgnfsgn",True)


