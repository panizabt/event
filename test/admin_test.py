from controller.admin_controller import AdminController
from model.entity import *

# database
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.create_all(engine)

# todo : error
AdminController.save("ali","hossieni","ali","ali123", "0001")
AdminController.edit("1","ali","alipour","ali","ali123", "0001")
# AdminController.edit("ali","alipour","ali","ali123", "0001")




# Admin(1,"ali","hossieni","ali","ali123", "0001")
# print(AdminController.edit(1 ,"ali", "alipour", "ali", "ali123", "0001"))