from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from controller.customer_controller import CustomerController
from model.entity.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# todo : error
#CustomerController.save("ali","abedi","aliiiabedi","ali123",
            #            "gharb",123456789,12345678)

CustomerController.save("reza","rezaii","rez","reza123",
                        "shargh",123456788,12345677)

