from sqlalchemy.orm import relationship

from model.entity.base import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Event(Base):
    __tablename__ = "events_tbl"

    
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title_date = Column("title_date", DateTime)
    _start_time = Column("start_time", DateTime)
    _end_date_time = Column("end_date_time", DateTime)
    _event_type = Column("event_type", String(20), nullable=False)
    _duration = Column("duration", Integer, nullable=False)
    _description = Column("description", String(100), nullable=False)
    _price = Column("price", Integer, nullable=False)

    _ticket = Column("ticket", Integer, nullable=False)
    ticket = relationship("Ticket", back_populates="events")

    _salon = Column("salon", String(30), nullable=False)
    salon = relationship("Salon", back_populates="events")
    
    def __init__(self, id, title_date, start_time,  end_date_time, event_type, duration, description, price):
        
        self.id = id
        self.title_date = title_date
        self.start_time = start_time
        self.end_date_time = end_date_time
        self.event_type = event_type
        self.duration = duration
        self.description = description
        self.price = price
    
    
    @property
    def id(self):
        return self.id
    
    
    @id.setter
    def id(self, id):
        self.id = id
    
    
    @property
    def title_date(self):
        return self.title_date
    
    
    @title_date.setter
    def title_date(self, title_date):
        self.title_date = title_date


    @property
    def start_time(self):
        return self.start_time


    @start_time.setter
    def start_time(self, start_time):
        self.start_time = start_time


    @property
    def end_date_time(self):
        return self.end_date_time
    
    
    @end_date_time.setter
    def end_date_time(self, end_date_time):
        self.end_date_time = end_date_time
    
    
    @property
    def event_type(self):
        return self.event_type
    
    
    @event_type.setter
    def event_type(self, event_type):
        self.event_type = event_type
    
    
    @property
    def duration(self):
        return self.duration
    
    
    @duration.setter
    def duration(self, duration):
        self.duration = duration
    
    
    @property
    def description(self):
        return self.description
    
    
    @description.setter
    def description(self, description):
        self.description = description


#test2
