from model.entity import *
from model.service import PaymentService
from model.tools import *


class PaymentController:

    @classmethod
    @exception_handling
    def save(cls, amount, date_time, payment_type, description):
        payment = Payment(None, amount, date_time, payment_type, description)
        PaymentService.save(payment)
        return payment

    @classmethod
    @exception_handling
    def edit(cls, id, amount, date_time, payment_type, description):
        payment = Payment(id, amount, date_time, payment_type, description)
        PaymentService.edit(payment)
        return payment

    @classmethod
    @exception_handling
    def remove(cls, id):
        old_payment = PaymentService.remove(id)
        return  old_payment

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
