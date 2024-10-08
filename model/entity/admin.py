import Base
import admin_validator

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
        self._username = Validation.name_validator(username, "Invalid Username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validation.name_validator(password, "Invalid Password")

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        self._access_level = Validation.int_validator(access_level, "Invalid Access Level")
