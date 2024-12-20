from model.entity import Ticket
from model.service import TicketService
from model.tools import exception_handling


class TicketController:

    @classmethod
    @exception_handling
    def save(cls, title, start_date, duration, event, price, payment, customer):
        ticket = Ticket(None, title, start_date, duration, event, price, payment, customer)
        TicketService.save(ticket)
        return Ticket

    @classmethod
    @exception_handling
    def edit(cls, id, title, start_date, duration, event, price, payment, customer):
        ticket = Ticket(id, title, start_date, duration, event, price, payment, customer)
        TicketService.edit(ticket)
        return Ticket

    @classmethod
    @exception_handling
    def remove(cls, id):
        old_ticket = TicketService.remove(id)
        return old_ticket

    @classmethod
    @exception_handling
    def find_all(cls):
        tickets = TicketService.find_all()
        return tickets

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        ticket = TicketService.find_by_id(id)
        return ticket

    @classmethod
    @exception_handling
    def find_by_customer(cls, customer_id):
        ticket = TicketService.find_by_customer(customer_id)
        return ticket

    @classmethod
    @exception_handling
    def find_by_event(cls, event_id):
        ticket = TicketService.find_by_event(event_id)
        return ticket
