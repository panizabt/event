from model.entity.ticket import Ticket
from model.repository.crud_repository import CrudRepository


class TicketService:
    repo = CrudRepository(Ticket)

    @classmethod
    def save (cls, ticket):
        cls.repo.save(ticket)

    @classmethod
    def edit(cls, ticket):
        cls.repo.edit(ticket)

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
    def find_by_customer(cls, customer):
        return cls.repo.find_by_customer(customer)

    @classmethod
    def find_by_event(cls, event):
        return cls.repo.find_by_event(event)
