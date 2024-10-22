from model.entity import Ticket
from model.repository import CrudRepository


class TicketService:
    repo = CrudRepository(Ticket)

    @classmethod
    def save(cls, ticket):
       return cls.repo.save(ticket)

    @classmethod
    def edit(cls, ticket):
        return cls.repo.edit(ticket)

    @classmethod
    def remove(cls, ticket_id):
        return cls.repo.remove(ticket_id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, ticket_id):
        return cls.repo.find_by_id(ticket_id)

    @classmethod
    def find_by_customer(cls, customer_id):
        return cls.repo.find_by(Ticket._customer_id == customer_id)

    @classmethod
    def find_by_event(cls, event_id):
        return cls.repo.find_by(Ticket._event_id == event_id)
