from model.entity import Admin
from model.repository import CrudRepository


class AdminService:
    repo = CrudRepository(Admin)

    @classmethod
    def save(cls, admin):
        cls.repo.save(admin)

    @classmethod
    def edit(cls, admin):
        cls.repo.edit(admin)

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
    def find_by(cls, by):
        return cls.repo.find_by(by)