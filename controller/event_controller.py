from model.entity.event import Event
from model.service.event_service import EventService
from model.tools.decorator import exception_handling


class EventController:

@classmethod
@exception_handling
def save(cls, title_date, start_time, end_date_time, event_type, duration, description, price):
        event = Event(None, title_date, start_time, end_date_time, event_type, duration, description, price)
        EventService.save(event)
        return  "Event saved"


@classmethod
@exception_handling
def edit(cls, id, title_date, start_time, end_date_time, event_type, duration, description, price):
        event = Event(id, title_date, start_time, end_date_time, event_type, duration, description, price)
        EventService.edit(Event)
        return  "Event edited"


@classmethod
@exception_handling
def remove(cls, id):
        event = Event(id)
        EventService.remove(event)
        return True, "Event removed"


@classmethod
@exception_handling
def find_all(cls):
        return True, EventService.find_all()


@classmethod
@exception_handling
def find_by_title(cls, title_date):
       return EventService.find_by_title(title_date)


@classmethod
@exception_handling
def find_by_date_time(cls, start_date_time, end_date_time):
       return  EventService.find_by_date_time(start_date_time, end_date_time)


@classmethod
@exception_handling
def find_by_salon(cls, description):
 return EventService.find_by_salon(description)



