from datetime import datetime
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.salon_controller import SalonController
from view.component import *


class SalonView:
    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.location.set("")
        self.capacity.set(0)
        self.availability.set("")
        self.table.refresh_table(SalonController.find_all()[1])

    @staticmethod
    def table_click(self, selected_item):
        self.id.set(selected_item[0])
        self.title.set(selected_item[1])
        self.location.set(selected_item[2])
        self.capacity.set(selected_item[3])
        self.availability.set(selected_item[4])

    def save_click(self):
        status, message = SalonController.edit(
            self.id.get(),
            self.title.get(),
            self.location.get(),
            self.capacity.get(),
            self.availability.get(),
        )
        if status:
            msg.showinfo("Salon Saved", message)
            self.reset_form()
        else:
            msg.showerror("Salon Save", message)

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
        if msg.askyesno("Remove Salon?", "Are you sure?"):
            status, message = SalonController.remove(self.id.get())
            if status:
                msg.showinfo("Salon Removed", message)
                self.reset_form()

            else:
                msg.showerror("Salon Remove", message)

    def __init__(self):
        win = Tk()
        win.title("Salon View")
        win.geometry("1000x500")

        self.id = LabelWithEntry(win, "id", 50, 20, data_type="int")
        self.title = LabelWithEntry(win, "title", 50, 60, data_type="str")
        self.location = LabelWithEntry(win, "location", 50, 100, data_type="str")
        self.capacity = LabelWithEntry(win, "capacity", 50, 140, data_type="str")
        self.availability = LabelWithEntry(win, "availability", 50, 180, data_type="int")

        self.table = Table(win,
                           ["id", "title", "location", "capacity", "availability"],
                           [60, 120, 120, 120, 150, 80, 180, 100], 400, 20, self.table_click)

        Button(win, text="Save", width=10, bg="white", command=self.save_click).place(x=50, y=300)
        Button(win, text="Edit", width=10, bg="green", command=self.edit_click).place(x=150, y=300)
        Button(win, text="Remove", width=10, bg="yellow", command=self.remove_click).place(x=250, y=300)


        self.reset_form()
        win.mainloop()

