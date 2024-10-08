from model.entity.event import Event
from model.repository.crud_repository import CrudRepository


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
        return cls.repo.find_by_title(title)

    @classmethod
    def find_by_date_time(cls, date_time):
        return cls.repo.date_time(date_time)

    @classmethod
    def find_by_salon(cls, salon):
       return cls.repo.find_by_salon(salon)


#test