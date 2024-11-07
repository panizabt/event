from model.entity import *
from model.tools import *


class Event(Base):
    __tablename__ = "event_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(50))
    _start_date_time = Column("start_date_time", DateTime)
    _end_date_time = Column("end_date_time", DateTime)
    _event_type = Column("event_type", String(20), nullable=False)
    _duration = Column("duration", Integer)
    _description = Column("description", String(100))
    _price = Column("price", Integer, nullable=False)
    

    ticket = relationship("Ticket", back_populates="event")

    _salon_id = Column("salon_id", Integer, ForeignKey("salon_tbl.id"))
    salon = relationship("Salon", cascade="all")

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
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = Validation.title_validator(title, "Invalid title")

    @property
    def start_date_time(self):
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        self._start_date_time = Validation.start_time_validator(start_date_time, "Invalid start_date_time")

    @property
    def end_date_time(self):
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        self._end_date_time = Validation.end_time_validator(end_date_time, "Invalid end_date_time")

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        self._event_type = Validation.event_type_validator(event_type, "Invalid event_type")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = Validation.duration_validator(duration, "Invalid duration")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = Validation.description_validator(description, "Invalid description")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = Validation.price_validator(price, "Invalid price")
