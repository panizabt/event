from model.entity.salon import Salon
from model.service import salon_service
from model.service.salon_service import SalonService
from model.tools.decorator import exception_handling


class SalonController:
    @classmethod
    @exception_handling
    def save(cls, title, location, capacity, description, is_available):
        saloon = Salon(None, title, location, capacity, description, is_available)
        SalonService.save(saloon)
        return saloon

    @classmethod
    @exception_handling
    def edit(cls, id, title, location, capacity, description, is_available):
        salon = Salon(id, title, location, capacity, description, is_available)
        SalonService.edit(salon)
        return salon

    @classmethod
    @exception_handling
    def remove(cls, id):
        old_salon = SalonService.remove(id)
        return old_salon

    @classmethod
    @exception_handling
    def find_all(cls):
        return SalonService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return SalonService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_title(cls, title):
        return SalonService.find_by_title(title)

    @classmethod
    @exception_handling
    def have_capacity(cls, capacity):
        return SalonService.have_capacity(capacity)

    @classmethod
    @exception_handling
    def find_by_availability(cls, availability):
        return SalonService.find_by_available(availability)
