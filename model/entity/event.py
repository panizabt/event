from model.entity import *
from model.tools import *


class Event(Base):
    __tablename__ = "events_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title_date", String(50))
    _start_date_time = Column("start_date_time", DateTime)
    _end_date_time = Column("end_date_time", DateTime)
    _event_type = Column("event_type", String(20), nullable=False)
    _duration = Column("duration", Integer, nullable=False)
    _description = Column("description", String(100), nullable=False)
    _price = Column("price", Integer, nullable=False)

    _ticket = Column("ticket_id", Integer, ForeignKey("ticket_tbl.id"))
    ticket = relationship("Ticket", back_populates="event")

    _salon = Column("salon", Integer, ForeignKey("salon_tbl.id"))
    salon = relationship("Salon", back_populates="event")

    def __init__(self, id, title, start_date_time, end_date_time, event_type, duration, description, price, salon):
        self.id = id
        self.title = title
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.event_type = event_type
        self.duration = duration
        self.description = description
        self.price = price
        self.salon = salon

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = id

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, title):
        self.title = Validation.title_validator(title, "Invalid Title")

    @property
    def start_time(self):
        return self.start_time

    @start_time.setter
    def start_time(self, start_time):
        self.start_time = Validation.start_time_validator(start_time, "Invalid start_time")

    @property
    def end_date_time(self):
        return self.end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        self.end_date_time = Validation.end_time_validator(end_date_time, "Invalid end_date_time")

    @property
    def event_type(self):
        return self.event_type

    @event_type.setter
    def event_type(self, event_type):
        self.event_type = Validation.event_type_validator(event_type, "Invalid event_type")

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, duration):
        self.duration = Validation.duration_validator(duration, "Invalid duration")

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, description):
        self.description = Validation.description_validator(description, "Invalid description")

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        self.price = Validation.price_validator(price, "Invalid price")
