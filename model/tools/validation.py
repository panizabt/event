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
    def family_validator(family, message):
        if type(family) == str and re.match(r"^[a-zA-Z\s]{2,30}$", family):
            return family
        else:
            raise ValueError(message)

    @staticmethod
    def username_validator(username, message):
        if type(username) == str and re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @staticmethod
    def address_validator(address, message):
        if type(address) == str and re.match(r"^[\wa-zA-Z\s]{2,30}$", address):
            return address
        else:
            raise ValueError(message)



    @staticmethod
    def password_validator(password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @staticmethod
    def phone_validator(phone, message):
        if re.match(r"^[\w0-9\s]{2,16}$", phone):
            return phone
        else:
            raise ValueError(message)

    @staticmethod
    def postal_code_validator(postal_cod, message):
        if re.match(r"^[\w0-9\s]{2,16}$", postal_cod):
            return postal_cod
        else:
            raise ValueError(message)


    @staticmethod
    def address_validator(address, message):
        if type(address) == str and re.match(r"^[a-zA-Z\s]{2,30}$", address):
            pass

    # --------

    @staticmethod
    def title_validator(title, message):
        if type(title) == date and re.match(r"^[0-9]$", title):
            return title
        else:
            raise ValueError(message)

    @staticmethod
    def start_time_validator(start_time, message):
        if type(start_time) == datetime:
            return start_time
        else:
            raise ValueError(message)

    @staticmethod
    def end_time_validator(end_date_time, message):
        if type(end_date_time) == datetime:
            return end_date_time
        else:
            raise ValueError(message)

    @staticmethod
    def price_validator(price, message):
        if type(price) == int and price>0:
            return price
        else:
            raise ValueError(message)

    @staticmethod
    def description_validator(description, message):
        if re.match(r"^[0-9a-zA-Z\s]{1,100}$", description):
            return description
        else:
            raise ValueError(message)

    @staticmethod
    def duration_validator(duration, message):
        if type(duration) == int and duration > 0:
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

    @staticmethod
    def payment_amount_validator(amount, message):
        if type(amount) == int and amount > 0:
            return amount
        else:
            raise ValueError(message)

    @staticmethod
    def payment_type_validator(payment_type, message):
        if type(payment_type) == str and re.match(r"^[0-9a-zA-Z\s]{1,30}$", payment_type):
            return payment_type
        else:
            raise ValueError(message)

    @staticmethod
    def payment_description_validator(cls, description, message):
        if re.match(r"^[0-9a-zA-Z\s]{1,30}$", description):
            return description
        else:
            raise ValueError(message)




