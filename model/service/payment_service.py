from model.entity.payment import Payment
from model.repository.crud_repository import CrudRepository


class PaymentService:
    repo = CrudRepository(Payment)

    @classmethod
    def save(cls, payment):
        cls.repo.save(payment)
        return payment

    @classmethod
    def edit(cls, payment):
        cls.repo.edit(payment)
        return payment

    @classmethod
    def remove(cls, id):
        cls.repo.remove(id)
        return id

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by_ticket(cls, ticket_id):
        return cls.repo.find_by(Payment._ticket_id == ticket_id)

    @classmethod
    def find_by_data_time(cls, data_time):
        return cls.repo.find_by_data_time(data_time)

    @classmethod
    def find_by_payment_type(cls, payment_type):
        return cls.repo.find_by_payment_type(Payment._payment_type == payment_type)