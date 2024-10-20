from model.entity import *
from model.service import PaymentService
from model.tools import *


class PaymentController:

    @classmethod
    @exception_handling
    def save(cls, amount, date_time, payment_type, description):
        pay = Payment(None, amount, date_time, payment_type, description)
        PaymentService.save(pay)
        return "Payment saved"

    @classmethod
    @exception_handling
    def edit(cls, id, amount, date_time, payment_type, description):
        pay = Payment(id, amount, date_time, payment_type, description)
        PaymentService.edit(pay)
        return "Payment Has Been Edited!"

    @classmethod
    @exception_handling
    def remove(cls, id):
        PaymentService.remove(id)
        return  "Info: Payment Removed!"

    @classmethod
    @exception_handling
    def find_all(cls):
        return  PaymentService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return  PaymentService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_ticket(cls, ticket_id):
        return  PaymentService.find_by_ticket(ticket_id)

    @classmethod
    @exception_handling
    def find_by_data_time(cls, data_time):
        return  PaymentService.find_by_data_time(data_time)

    @classmethod
    @exception_handling
    def find_by_payment_type(cls, payment_type):
        return  PaymentService.find_by_payment_type(payment_type)
