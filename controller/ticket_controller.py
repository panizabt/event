from model.entity import Ticket
from model.service import TicketService
from model.tools import exception_handling


class TicketController:

    @classmethod
    @exception_handling
    def save(cls, title, start_date, duration, event, price, payment, customer_id):
        ticket = Ticket(None, title, start_date, duration, event, price, payment, customer_id)
        TicketService.save(ticket)
        return "Ticket Saved"

    @classmethod
    @exception_handling
    def edit(cls, id, title, start_date, duration, event, price, payment, customer_id):
        ticket = Ticket(id, title, start_date, duration, event, price, payment, customer_id)
        TicketService.edit(ticket)
        return "Ticket Edited"

    @classmethod
    @exception_handling
    def remove(cls, id):
        TicketService.remove(id)
        return "Ticket Removed"

    @classmethod
    @exception_handling
    def find_all(cls):
        tickets = TicketService.find_all()
        return  tickets

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        ticket = TicketService.find_by_id(id)
        return  ticket

    @classmethod
    @exception_handling
    def find_by_customer(cls, customer_id):
        tickets = TicketService.find_by_customer(customer_id)
        return  tickets

    @classmethod
    @exception_handling
    def find_by_event(cls, event_id):
        tickets = TicketService.find_by_event(event_id)
        return  tickets
