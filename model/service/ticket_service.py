from model.entity.ticket import Ticket
from model.repository.crud_repository import CrudRepository

class TicketService:
    repo = CrudRepository(Ticket)

    @classmethod
    def save(cls, ticket):
        cls.repo.save(ticket)

    @classmethod
    def edit(cls, ticket):
        cls.repo.edit(ticket)

    @classmethod
    def remove(cls, ticket_id):
        cls.repo.remove(ticket_id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, ticket_id):
        return cls.repo.find_by_id(ticket_id)

    @classmethod
    def find_by_customer(cls, customer_id):
        return cls.repo.find_by(Ticket.customer_id == customer_id)

    @classmethod
    def find_by_event(cls, event_id):
        return cls.repo.find_by(Ticket.event_id == event_id)
