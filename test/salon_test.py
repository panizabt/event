from model.entity import *
from controller import SalonController
from view.salon_view import SalonView

SalonController.save("aria","teh",300,"fgded",True)
# SalonController.edit()
# print(SalonController.find_all())
print(SalonController.find_by_id(1))
#SalonController.edit("aria","teh",300,"fgded",True)
# todo : test edit, remove, find_all , find_by_id, find_by_location

SalonView()