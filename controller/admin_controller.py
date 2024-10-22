from model.tools import exception_handling
from model.entity import Admin
from model.service import AdminService


class AdminController:    

    @classmethod
    @exception_handling
    def save(cls, name, surname, username, password, access_level):
            admin = Admin(None, name, surname, username, password, access_level)
            AdminService.save(admin)
            return admin


    @classmethod
    @exception_handling
    def edit(cls, id, name, surname, username, password, access_level):
            admin = Admin(id, name, surname, username, password, access_level)
            AdminService.edit(admin)
            return admin


    @classmethod
    @exception_handling
    def remove(cls, id):
            old_admin = AdminService.remove(id)
            return old_admin


    @classmethod
    @exception_handling
    def find_all(cls):
            return AdminService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
            return AdminService.find_by_id(id)

    # todo : find by username
    # todo : find by username and password