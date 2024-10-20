from datetime import datetime
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from  controller.salon_controller import SalonController

class SalonView:
    def resert(self):
        self.id.set(0)
        self.title(0)
        self.location.set("")
        self.capacity("")
        self.availability("")

    @staticmethod
    def table_click(selected_item):
        print(selected_item)

    def save_record(self):
        status, message = SalonController.save(self.amount.get(), self.date.get(),
                                                 self.salon_type.get(), self.description.get())
        if status:
            msg.showinfo("Saved.", message)
            self.reset_form()
        else:
            msg.showerror("Save Error!", message)

    def remove_record(self):
        if msg.askyesno("Remove Salon!", "Are you sure?"):
            status, message = SalonController.remove(self.id.get())
            if status:
                msg.showinfo("Removed.", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error!", message)

    def edit_record(self):
        status, message = SalonController.edit(self.id.get(), self.amount.get(), self.date.get(),
                                                 self.salon_type.get(), self.description.get())
        if status:
            msg.showinfo("Edited.", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error!", message)
