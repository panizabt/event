from model.entity.ticket import Ticket
from model.service.ticket_service import TicketService

class TicketController:

    @classmethod
    def save(cls, title, start_time, duration, event, price, payment, customer_id):
        try:
            ticket = Ticket(None, title, start_time, duration, event, price, payment, customer_id)
            TicketService.save(ticket)
            return True, "Ticket saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, ticket_id, title, start_time, duration, event, price, payment, customer_id):
        try:
            ticket = Ticket(ticket_id, title, start_time, duration, event, price, payment, customer_id)
            TicketService.edit(ticket)
            return True, "Ticket edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, ticket_id):
        try:
            TicketService.remove(ticket_id)
            return True, "Ticket Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, TicketService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, ticket_id):
        try:
            ticket = TicketService.find_by_id(ticket_id)
            if ticket:
                return True, ticket
            else:
                return False, "Ticket not found"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_customer(cls, customer_id):
        try:
            tickets = TicketService.find_by_customer(customer_id)
            if tickets:
                return True, tickets
            else:
                return False, "No tickets found for this customer"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_event(cls, event_id):
        try:
            tickets = TicketService.find_by_event(event_id)
            if tickets:
                return True, tickets
            else:
                return False, "No tickets found for this event"
        except Exception as e:
            return False, str(e)