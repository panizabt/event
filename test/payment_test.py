from datetime import datetime

from model.entity.payment import Payment
from model.service.payment_service import PaymentService
from controller.payment_controller import PaymentController
#app
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from model.entity.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# todo : error
d_t = datetime(2024,11,12,20,17,30)
PaymentController.save(10000, d_t, "income", "Desc")

PaymentController.save(15432, d_t, "expense", "Desc")

PaymentController.remove(1)

PaymentController.find_all()

PaymentController.find_by_id(1)