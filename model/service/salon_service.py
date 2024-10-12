from git import repo

from model.entity.salon import Salon
from model.repository.crud_repository import CrudRepository

class SalonService:
    repo = CrudRepository(Salon)

    @classmethod
    def save(cls,salon):
        cls.repo.save(salon)

    @classmethod
    def edit(cls,salon):
        cls.repo.edit(salon)

    @classmethod
    def remove(cls,salon):
        cls.repo.remove(salon)

    @classmethod
    def find_all(cls):
        cls.repo.find_all()

    @classmethod
    def find_by_id(cls,id):
        cls.repo.find_by_id(id)

    @classmethod
    def find_by_title(cls,title):
        cls.repo.find_by(Salon._title == title)

    @classmethod
    def have_capacity(cls,capacity):
        cls.repo.find_by(Salon._capacity == capacity)
