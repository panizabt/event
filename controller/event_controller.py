from model.entity import *
from model.service.event_service import EventService
from model.tools.decorator import *


class EventController:

    @classmethod
    @exception_handling
    def save(cls, title, start_date_time, end_date_time, event_type, duration, description, price, salon):
            event = Event(None, title, start_date_time, end_date_time, event_type, duration, description, price, salon)
            print(event)
            EventService.save(event)
            return  "Event saved"


    @classmethod
    @exception_handling
    def edit(cls, id, title, start_date_time, end_date_time, event_type, duration, description, price):
            event = Event(id, title, start_date_time, end_date_time, event_type, duration, description, price, salon)
            EventService.edit(Event)
            return  "Event edited"


    @classmethod
    @exception_handling
    def remove(cls, id):
            EventService.remove(id)
            return True, "Event removed"


    @classmethod
    @exception_handling
    def find_all(cls):
            return True, EventService.find_all()


    @classmethod
    @exception_handling
    def find_by_title(cls, title):
           return EventService.find_by_title(title)


    @classmethod
    @exception_handling
    def find_by_date_time(cls, start_date_time):
           return  EventService.find_by_date_time(start_date_time)


    # todo : error
    @classmethod
    @exception_handling
    def find_by_salon(cls, salon_id):
        return EventService.find_by_salon(salon_id)





