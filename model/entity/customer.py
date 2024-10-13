from model.entity.base import Base
from tools import validation
from sqlalchemy import Column, Integer, String


class Customer(Base):
    __tablename__ = "costumer_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _username = Column("username", String(20), nullable=False)
    _password = Column("password", String(255), nullable=False)
    _address = Column("address", String(255), nullable=False)
    _phone = Column("phone", String(20), nullable=False)
    _postal_code = Column("postal_code", String(20), nullable=False)


    def __init__(self, id, name, family, username, password, address, phone, postal_code):
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.address = address
        self.phone = phone
        self.postal_code = postal_code

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validation.name_validator(name, "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validation.family_validator(family, "Invalid Family")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
