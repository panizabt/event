from controller.salon_controller import SalonController

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from model.entity.base import Base

connection = "mysql+pymysql://root:123456@localhost:3306/mft"
if not database_exists(connection):
    create_database(connection)

engine=create_engine(connection)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


SalonController.save(1,"aria","teh",300,"fgded",True)