import re
from datetime import datetime,date


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if type(name) ==  str and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if type(username) ==  str and re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def address_validator(cls, address, message):
        if type(address) == str and re.match(r"^[a-zA-Z\s]{2,30}$", address):
            return address

    @classmethod
    def postal_code_validator(cls, postal_code, message):
        if type(postal_code) == str and re.match(r"^[0-9\s]{10}$", postal_code):
            return postal_code
    @classmethod
    def family_validator(cls, family, message):
        if type(family) == str and re.match(r"^[a-zA-Z\s]{2,30}$", family):
            return family

    @classmethod
    def phone_validator(cls, phone, message):
        if type(phone) == str and re.match(r"^[0-9\s]{8}$", phone):
            return phone
