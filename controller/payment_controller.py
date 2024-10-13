from model.entity.payment import Payment
from model.service.payment_service import PaymentService


class PaymentController:

    @classmethod
    def save(cls,  id, amount, date_time, payment_type,description):
        # payment entity setter
        try:
            pay = Payment(None, amount, date_time, payment_type,description)
            PaymentService.save(pay)
            return True, "Info: Transaction has been done !"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, amount, date_time, payment_type, description):
        try:
            pay = Payment(id, amount, date_time, payment_type, description)
            PaymentService.edit(pay)
            return True, "Payment Has Been Edited!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            PaymentService.remove(id)
            return True, "Info: Payment Removed!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, PaymentService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, PaymentService.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_ticket(cls, ticket_id):
        try:
            return True, PaymentService.find_by_ticket(ticket_id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_data_time(cls, data_time):
        try:
            return True, PaymentService.find_by_data_time(data_time)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_payment_type(cls, payment_type):
        try:
            return True, PaymentService.find_by_payment_type(payment_type)
        except Exception as e:
            return False, str(e)