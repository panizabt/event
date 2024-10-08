from model.entity.ticket import Ticket
from model.service.ticket_service import TicketService

class TicketController:

    @classmethod
    def save(cls, title, start_time, duration, event, price, payment, customer_id ):
        try:
            ticket = Ticket(None, title, start_time, duration, event, price, payment, customer_id)
            TicketService.save(ticket)
            return True, "Ticket saved"

        except Exception as e:
            return False, str(e)
    @classmethod
    def edit(cls, title, start_time, duration, event, price, payment, customer_id ):
        try:
            ticket = Ticket(None, title, start_time, duration, event, price, payment, customer_id)
            TicketService.edit(ticket)
            return True, "Ticket edited"

        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, title, start_time, duration, event, price, payment, customer_id ):
        try:
            TicketService.remove(id)
            return True, "Ticket Removed"
        except Exception as e:
            return False, str(e)
