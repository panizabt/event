from model.entity.salon import Salon
from model.service import salon_service
from model.service.salon_service import SalonService
from model.tools.decorator import exception_handling


class SalonController:
    @classmethod
    @exception_handling
    def save(cls,id,title,location,capacity,description,is_available):

            saloon=Salon(None,title,location,capacity,description,is_available)
            SalonService.save(saloon)
            return "Saloon Saved"



    @classmethod
    @exception_handling
    def edit(cls,salon_id,title,location,capacity,description,is_available):
        salon=Salon(None,title,location,capacity,description,is_available)
        return "Salon edited"

    @classmethod
    @exception_handling
    def remove(cls,salon_id):
        SalonService.remove(salon_id)
        return "Salon removed"

    @classmethod
    @exception_handling
    def find_all(cls):
        return SalonService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls,salon_id):
        return SalonService.find_by_id(salon_id)

    @classmethod
    @exception_handling
    def find_by_title(cls,title):
        return SalonService.find_by_title(title)



    @classmethod
    @exception_handling
    def have_capacity(cls,capacity):
        return SalonService.have_capacity(capacity)

    @classmethod
    @exception_handling
    def find_by_availability(cls,availability):
        return  SalonService.find_by_available(availability)



