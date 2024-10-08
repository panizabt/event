import Base
from tools import validator


class Admin(Base):
    __tablename__ = 'admin'
    _id = Column(Integer, primary_key=True)
    _name = Column(String, nullable=False)
    _surname = Column(String, nullable=False)
    _username = Column(String, nullable=False)
    _password = Column(String, nullable=False)
    _access_level = Column(Integer, nullable=False)

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
        self._name = validator.name_validator(name, "Invalid Name")

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = validator.no_numbers(surname, "Invalid Surname")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = validator.name_validator(username, "Invalid Username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = validator.name_validator(password, "Invalid Password")

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        self._access_level = validator.int_validator(access_level, "Invalid Access Level")
