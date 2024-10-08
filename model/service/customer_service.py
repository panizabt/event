from model.entity.customer import Customer
from model.repository.crud_repository import CrudRepository


class CostumerService:
    repo = CrudRepository(Customer)

    @classmethod
    def save(cls, customer):
        cls.repo.save(customer)

    @classmethod
    def edit(cls, customer):
        cls.repo.edit(customer)

    @classmethod
    def remove(cls, id):
        cls.repo.remove(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by_username(cls, username):
        return cls.repo.find_by_username(username)

    @classmethod
    def find_by_password(cls, password):
        return cls.repo.find_by_password(password)

    @classmethod
    def find_by_name(cls, name):
        return cls.repo.find_by_name(name)

    @classmethod
    def find_by_family(cls, family):
        return cls.repo.find_by_family(family)
