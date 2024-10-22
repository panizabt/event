from model.entity import *
from controller import TicketController, PaymentController, CustomerController, EventController
from view.ticket_view import TicketView

# test : error
start_date = datetime(2024, 11, 12, 20, 17, 30)
# ticket = Ticket(None, "title", start_date, 15, None, 10000, None, None)

d_t = datetime(2024, 11, 12, 20, 17, 30)
_, payment = PaymentController.save(10000, d_t, "cardrgfgqreqdf", "Desc")

_, customer = CustomerController.save("reza", "rezaii", "rez", "reza123", "shargh", 123456788, 12345677)

s_t = datetime(2024,5,23,18,0,0)
e_t = datetime(2024,5,23,20,0,0)
_, event  = EventController.save("Concert ali",  s_t, e_t, "Consert", 120, "lotfan 2 saat zod tar hozor peyda konid", 650000, salon)


_, ticket = TicketController.save("concert", start_date, 90, event, 1000000, payment, customer)

# ui = TicketView()

# TicketController.edit(1, "concert", start_date, 90, "Concert music", 1000000, "Credit Card", 111)
#
# TicketController.remove(1)
#
# TicketController.find_all()
#
# TicketController.find_by_id(1)

# TicketController.find_by_customer(1)
#
# TicketController.find_by_event(1)
