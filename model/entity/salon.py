from sqlalchemy import Column, Integer,  String, Boolean


class Salon(Base):
    __tablename__ = "salon_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String)
    _location= Column("location", String)
    _capacity = Column("capacity", Integer)
    _description = Column("description", String)
    _isavailable= Column("isAvailable", Boolean)



    def __init__(self, id, title,location):
        self.id = id
        self.title = title
        self.location = location
        self.capacity = capacity
        self.description= description
        self.isavailable=isavailable