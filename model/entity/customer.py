from model.entity.base import Base
from sqlalchemy import Column, Integer, String
from model.tools import validation


class Customer(Base):
    __tablename__ = "costumer_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _username = Column("username", String(20), nullable=False)
    _password = Column("password", String(255), nullable=False)
    _address = Column("address", String(255), nullable=False)
    _phone = Column("phone", Integer, nullable=False)
    _postal_code = Column("postal_code", Integer, nullable=False)


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
        self._name = validation.name_validator(name, "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = validation.family_validator(family, "Invalid Family")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = validation.username_validator(username, "Invalid Username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = validation.password_validator(password, "Invalid Password")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = validation.address_validator(address, "Invalid Address")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = validation.phone_validator(phone, "Invalid Phone")

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = validation.postal_code_validator(postal_code, "Invalid Postal Code")
        #111
