from model.entity.payment import Payment
from model.repository.crud_repository import CrudRepository


class PaymentService:
    repo = CrudRepository(Payment)

    @classmethod
    def save(cls, payment):
        cls.repo.save(payment)
        return payment

    @classmethod
    def save(cls, id):
        cls.repo.save(id)
        return id

    @classmethod
    def edit(cls, payment_type):
        cls.repo.edit(payment_type)
        return payment_type

    @classmethod
    def save(cls, amount):
        cls.repo.save(amount)
        return amount

    @classmethod
    def save(cls, date_time):
        cls.repo.save(date_time)
        return date_time

    @classmethod
    def save(cls, description):
        cls.repo.save(description)
        return description


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
        return cls.repo.find_by_ticket(ticket_id)

    @classmethod
    def find_by_data_time(cls, data_time):
        return cls.repo.find_by_data_time(data_time)

    @classmethod
    def find_by_payment_type(cls, payment_type):
        return cls.repo.find_by_payment_type(payment_type)