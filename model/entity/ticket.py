from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base


class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(20), nullable=False)
    _start_date = Column("start_date", Date, nullable=False)
    _duration = Column("duration", Integer, nullable=False)
    _price = Column("price", Integer, nullable=False)

    _customer_id = Column("customer_id", Integer, ForeignKey("customer.id"))
    customer = relationship("Customer")

    _payment_id = Column("payment", Integer, ForeignKey("payment_tbl.id"))
    payment = relationship("Payment", back_populates="ticket")

    _event_id = Column("event", Integer, ForeignKey("event_tbl.id"))
    event = relationship("Event")

    def __init__(self, id, title, start_date, duration, event, price, payment, customer_id):
        self.id = id
        self.title = title
        self.start_date = start_date
        self.duration = duration
        self.event = event
        self.price = price
        self.payment = payment
        self.customer_id = customer_id

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
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, event):
        self._event = event

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment_relation(self, payment):
        self._payment = payment
