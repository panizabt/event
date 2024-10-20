from model.entity import *
from controller import TicketController


# test : error
start_date = datetime(2024, 11, 12, 20, 17, 30)
# ticket = Ticket(None, "title", start_date, 15, None, 10000, None, None)

TicketController.save("concert", start_date, 90, "concert music", 1000000, "Credit Card", 111)

TicketController.edit(1, "concert",  start_date, 90, "Concert music", 1000000, "Credit Card", 111)

TicketController.remove(1)

TicketController.find_all()

TicketController.find_by_id(1)

# TicketController.find_by_customer(1)
#
# TicketController.find_by_event(1)
