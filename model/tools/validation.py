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

#--------

@staticmethod
 def title_date_validator(title_date, message):
    if type(title_date) == date and re.match(r"^[0-9]$", title_date):
        return title_date
    else:
        raise ValueError(message)
@staticmethod
 def start_time_validator(start_time, message):
    if type(start_time) == date and re.match(r"^[0-9]$", start_time):
        return start_time
    else:
        raise ValueError(message)
@staticmethod
 def end_time_validator(end_date_time, message):
     if type(end_date_time) == date and re.match(r"^[0-9]$", end_date_time):
         return end_date_time
     else:
         raise ValueError(message)
@staticmethod
def price_validator(price, message):
    if type(price) == int and re.match(r"^[0-9]{1,20}$", price):
        return price
    else:
        raise ValueError(message)
@staticmethod
def description_validator(description, message):
    if re.match(r"^[0-9a-zA-Z\s]{1,30}$", description):
        return description
    else:
        raise ValueError(message)
@staticmethod
def duration_validator(duration, message):
    if re.match(r"^[0-9a-zA-Z\s]{1,20}$", duration):
        return duration
    else:
        raise ValueError(message)
@staticmethod
def event_type_validator(event_type, message):
    if re.match(r"^[0-9a-zA-Z\s]{1,30}$", event_type):
        return event_type
    else:
        raise ValueError(message)



            
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
