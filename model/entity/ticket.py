from model.entity import *


class Ticket(Base):
    __tablename__ = "ticket_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(20), nullable=False)
    _start_date_time = Column("start_date_time", DateTime, nullable=False)
    _duration = Column("duration", Integer, nullable=False)
    _price = Column("price", Integer, nullable=False)

    # todo : check relations
    _customer_id = Column("customer_id", Integer, ForeignKey("customer_tbl.id"))
    customer = relationship("Customer")

    _payment_id = Column("payment_id", Integer, ForeignKey("payment_tbl.id"))
    payment = relationship("Payment")

    _event_id = Column("event_id", Integer, ForeignKey("event_tbl.id"))
    event = relationship("Event")

    def __init__(self, id, title, start_date_time, duration, event, price, payment, customer):
        self.id = id
        self.title = title
        self.start_date_time = start_date_time
        self.duration = duration
        self.event = event
        self.price = price
        self.payment = payment
        self.customer = customer

    # todo : setter validation
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def start_date_time(self):
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        self._start_date_time = start_date_time

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
