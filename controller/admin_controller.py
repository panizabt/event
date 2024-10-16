
from model.tools.decorator import exception_handling
from model.entity.admin import Admin
from model.service.admin_service import AdminService


class AdminController:    

    @classmethod
    @exception_handling
    def save(cls, name, surname, username, password, access_level):
            admin = Admin(None, name, surname, username, password, access_level)
            AdminService.save(admin)
            return "Admin Saved"


    @classmethod
    @exception_handling
    def edit(cls, id, name, surname, username, password, access_level):
            admin = Admin(id, name, surname, username, password, access_level)
            AdminService.edit(admin)
            return "Admin Edited"


    @classmethod
    @exception_handling
    def remove(cls, id):
            AdminService.remove(id)
            return "Admin Removed"


    @classmethod
    @exception_handling
    def find_all(cls):
            return AdminService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
            return AdminService.find_by_id(id)
