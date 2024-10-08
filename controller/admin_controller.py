

from model.entity.admin import Admin
from model.service.admin_service import AdminService


class AdminController:    

    @classmethod
    def save(cls, name, surname, username, password, access_level):
        try:
            admin = Admin(None, name, surname, username, password, access_level)
            AdminService.save(admin)
            return True, "Admin Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, surname, username, password, access_level):
        try:
            admin = Admin(id, name, surname, username, password, access_level)
            AdminService.edit(admin)
            return True, "Admin Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            AdminService.remove(id)
            return True, "Admin Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, AdminService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, AdminService.find_by_id(id)
        except Exception as e:
            return False, str(e)