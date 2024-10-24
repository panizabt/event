from model.entity import Customer
from model.service import CustomerService
from model.tools import exception_handling


class CustomerController:

    @classmethod
    @exception_handling
    def save(cls, name, family, username, password, address, phone, postal_code):
        customer = Customer(None, name, family, username, password, address, phone, postal_code)
        CustomerService.save(customer)
        return customer

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, username, password, address, phone, postal_code):
        customer = Customer(id, name, family, username, password, address, phone, postal_code)
        CustomerService.edit(customer)
        return customer

    @classmethod
    @exception_handling
    def remove(cls, id):
        old_customer = CustomerService.remove(id)
        return old_customer

    @classmethod
    @exception_handling
    def find_all(cls):
        return CustomerService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return CustomerService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return CustomerService.find_by_username(username)

    @classmethod
    @exception_handling
    def find_by_name(cls, name):
        return CustomerService.find_by_name(name)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return CustomerService.find_by_family(family)

    @classmethod
    @exception_handling
    def find_by_password(cls, password):
        return CustomerService.find_by_password(password)
