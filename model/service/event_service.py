from model.entity import Event
from model.repository import CrudRepository


class EventService:
    repo = CrudRepository(Event)

    @classmethod
    def save(cls, event):
        cls.repo.save(event)

    @classmethod
    def edit(cls, event):
        cls.repo.save(event)

    @classmethod
    def remove(cls, id):
        cls.repo.remove(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by_title(cls, title):
        return cls.repo.find_by(Event.title == title)

    @classmethod
    def find_by_date_time(cls, start_date_time):
        return cls.repo.find_by(Event.start_date_time == start_date_time)

    @classmethod
    def find_by_salon(cls, salon_id):
       return cls.repo.find_by(Event._salon_id == salon_id)


#test2