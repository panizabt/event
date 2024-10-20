from sqlalchemy import Column, Integer,  String, Boolean

from model.tools import*

class Salon(Base):
    __tablename__ = "salon_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(30))
    _location= Column("location", String(100))
    _capacity = Column("capacity", Integer)
    _description = Column("description", String(100))
    _is_available= Column("is_available", Boolean)


    def __init__(self, id, title,location,capacity,description, is_available):
        self.id = id
        self.title = title
        self.location = location
        self.capacity = capacity
        self.description= description
        self.isavailable=is_available

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
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        self._is_available = is_available






