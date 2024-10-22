from model.entity import *
from controller import PaymentController
from view.payment_view import PaymentView

# todo : error
d_t = datetime(2024,11,12,20,17,30)
PaymentController.save(10000, d_t, "cardrgfgqreqdf", "Desc")

PaymentController.save(15432, d_t, "cashfgfdgdqefg", "Desc")

PaymentController.save(1221345, d_t, "cashqerqedfgdfg", "Dessfgsgw")

#
PaymentController.find_all()
# #
PaymentController.find_by_id(1)
#
PaymentController.remove(1)


