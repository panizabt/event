from modle.entity.event import Event
from modle.service.event_service import EventService


class EventController

    @classmethod
    def save(cls, title_date, start_time, end_date_time, event_type, duration, description, price):
        try:
            event = Event(None, title_date, start_time, end_date_time, event_type, duration, description, price)
            EventService.save(event)
            return True, "Event saved"

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, title_date, start_time, end_date_time, event_type, duration, description, price):
        try:
            event = Event(id, title_date, start_time, end_date_time, event_type, duration, description, price)
            EventService.edit(Event)
            return True, "Event edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            event = Event(id)
            EventService.remove(event)
            return True, "Event removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, EventService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_title(cls, title_date):
        try:
            return True, EventService.find_by_title(title_date)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_date_time(cls, start_date_time, end_date_time):
        try:
            return True, EventService.find_by_date_time(start_date_time, end_date_time)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_salon(cls, description):
        try:
            return True, EventService.find_by_salon(description)
        except Exception as e:
            return False, str(e)
        
