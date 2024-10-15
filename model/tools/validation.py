import re
from datetime import datetime, date


class Validation:
    @staticmethod
    def name_validator(name, message):
        if type(name) == str and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @staticmethod
    def username_validator(username, message):
        if type(username) == str and re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @staticmethod
    def password_validator(password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @staticmethod
    def address_validator(address, message):
        if type(address) == str and re.match(r"^[a-zA-Z\s]{2,30}$", address):
            pass

    # --------

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

    @staticmethod
    def title_validator(title, message):
        if re.match(r"^[0-9a-zA-Z\s]{1,20}$", title):
            return title
        else:
            raise ValueError(message)


