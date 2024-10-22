from datetime import datetime
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from  controller.salon_controller import SalonController
from view.component import LabelWithEntry


class SalonView:
    def resert(self):
        self.id.set(0)
        self.title.set("")
        self.location.set("")
        self.capacity.set(0)
        self.availability.set("")

    @staticmethod
    def table_click(self,selected_item):
        self.id.set(selected_item[0])
        self.title.set(selected_item[1])
        self.location.set(selected_item[2])
        self.capacity.set(selected_item[3])
        self.availability.set(selected_item[4])


    def save_click(self):

        status,message=SalonController.edit(
            self.id.get(),
            self.title.get(),
            self.location.get(),
            self.capacity.get(),
            self.availability.get(),
        )
        if status:
            msg.showinfo("Salon Saved",message)
            self.reset_form()
        else:
            msg.showerror("Salon Save",message)

    def edit_click(self):
        status, message = SalonController.save(
            self.id.get(),
            self.title.get(),
            self.location.get(),
            self.capacity.get(),
            self.availability.get(),
        )
        if status:
            msg.showinfo("Salon Edited", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        if msg.askyesno("Remove Salon?","Are you sure?"):
            status, message=SalonController.remove(self.id.get())
            if status:
                msg.showinfo("Salon Removed",message)
                self.resert_form()

            else:
                msg.showerror("Salon Remove",message)

    def __init__(self):
        win = Tk()
        win.title("Event View")
        win.geometry("800x500")

        self.id =LabelWithEntry(win,"id",20,100,)





        Button(win, text="Save", command=self.save_record).place(x=100, y=220)
        Button(win, text="Remove", command=self.remove_record).place(x=100, y=250)
        Button(win, text="Edit", command=self.edit_record).place(x=100, y=280)


        win.mainloop()



