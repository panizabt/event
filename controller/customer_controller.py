import re

from model.entity.customer import Customer
from model.service.customer_service import CustomerService


class CustomerController:

    @classmethod
    def save(cls, name, family , username , password,address,phone,postal_code):
        try:
            customer = Customer( name, family, username, password, address, phone, postal_code)
            CustomerService.save(customer)
            return True, "Customer Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family,password,address,phone,postal_code):
        try:
            customer = Customer(id, name, family, password, address, phone, postal_code)
            CustomerService.edit(customer)
            return True, "Customer Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            CustomerService.remove(id)
            return True, "Customer Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, CustomerService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, CustomerService.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
         try:
              return True, CustomerService.find_by_username(username)
         except Exception as e:
              return False, str(e)

    @classmethod
    def find_by_name(cls, name):
        try:
            return True, CustomerService.find_by_name(name)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_family(cls, family):
        try:
            return True, CustomerService.find_by_family(family)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_password(cls, password):
        try:
            return True, CustomerService.find_by_password(password)
        except Exception as e:
            return False, str(e)



