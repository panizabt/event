from model.entity import Customer
from model.repository import CrudRepository


class CustomerService:
    repo = CrudRepository(Customer)

    @classmethod
    def save(cls, customer):
        return cls.repo.save(customer)

    @classmethod
    def edit(cls, customer):
        return cls.repo.edit(customer)

    @classmethod
    def remove(cls, id):
        return cls.repo.remove(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by_username(cls, username):
        return cls.repo.find_by(Customer.username == username)

    @classmethod
    def find_by_password(cls, password):
        return cls.repo.find_by_password(Customer.password == password) # todo : error

    @classmethod
    def find_by_name(cls, name):
        return cls.repo.find_by_name(Customer.name == name) # todo : error

    @classmethod
    def find_by_family(cls, family):
        return cls.repo.find_by_family(Customer.family == family) # todo : error
