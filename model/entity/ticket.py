from sqlalchemy import *
from model.entity.base import Base

class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(20), nullable=False)
    _start_date = Column("start_date", Date, nullable=False)
    _duration = Column("duration", Integer, nullable=False)
    _price = Column("price", Integer, nullable=False)

    _payment = Column("payment", Integer, nullable=False)
    _event = Column("event_relation", String(20), nullable=False)

    def __init__(self, id, title, start_date_time, duration, event, price , payment):
        self.id = id
        self.title = title
        self.start_date_time = start_date_time
        self.duration = duration
        self.event_relation = event_relation
        self.price = price
        self.payment_relation = payment_relation

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
        def event_relation(self):
            return self._event_relation

        @event_relation.setter
        def event_relation(self, event_relation):
            self._event_relation = event_relation

        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, price):
            self._price = price

        @property
        def payment_relation(self):
            return self._payment

        @payment_relation.setter
        def payment_relation(self, payment_relation):
            self._payment = payment_relation

