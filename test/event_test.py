from model.entity import *
from controller import EventController, SalonController

# todo : error
s_t = datetime(2024,5,23,18,0,0)
e_t = datetime(2024,5,23,20,0,0)

# SalonController.save("aria","teh",300,"fgded",True)
# status,salon = SalonController.find_by_id(1)
# print(status, salon)

salon = Salon( "aria","teh",300,"fgded",True)

EventController.save("Concert ali",  s_t, e_t, "Consert", 120, "lotfan 2 saat zod tar hozor peyda konid", 650000, salon)
#EventController.save("Film Reza",  s_t, e_t, "Film", 90, "lotfan 2 saat zod tar hozor peyda konid", 80000 ,None)
#EventController.edit(1, "concert alireza", s_t, e_t, "Concert", 120, "lotfan 2 saat zod tar hozor peyda konid", 650000, None)
#EventController.remove(1)
#EventController.find_all()
#EventController.find_by_title("Film Reza")
#EventController.find_by_date_time(s_t, e_t)
#EventController.find_by_salon(None)