from model.entity import *
from model.tools import Validation


class Admin(Base):
    __tablename__ = "admin_tbl"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(20), nullable=False)
    _surname = Column(String(20), nullable=False)
    _username = Column(String(20), nullable=False)
    _password = Column(String(20), nullable=False)
    _access_level = Column(String(10), nullable=False)

    def __init__(self, id, name, surname, username, password, access_level):
        self.id = id
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.access_level = access_level
        
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
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = Validation.name_validator(surname, "Invalid Surname")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = Validation.username_validator(username, "Invalid Username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validation.password_validator(password, "Invalid Password")

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        self._access_level = access_level
