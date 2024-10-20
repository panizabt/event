from model.entity import *
from model.tools import *

class Payment(Base):
    __tablename__ = "payment_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _amount = Column("amount", Float, nullable=False)
    _date_time = Column("date_time", DateTime, default=datetime.now)
    _payment_type = Column("payment_type", String(30), nullable=False)
    _description = Column("description", String(50), nullable=False)

    _ticket_id = Column("ticket_id", Integer, ForeignKey("ticket_tbl.id"))
    ticket = relationship("Ticket")

    # todo : setter validation

    def __init__(self, id, amount, date_time, payment_type, description):
        self.id = id
        self.amount = amount
        self.date_time = date_time
        self.payment_type = payment_type
        self.description = description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = Validation.payment_amount_validator(amount,"invalid payment amount")

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = date_time

    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        self._payment_type = Validation.payment_type_validator(payment_type,"Invalid payment type")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = Validation.payment_description_validator(description, "Invalid description")



