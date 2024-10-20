from tkinter import *
import tkinter.messagebox as msg
from controller.event_controller import EventController
from view.component import LabelWithEntry, Table


class AdminView:
    def reset_from(self):
        self.id.set(0)
        self.name.set("")
        self.surname.set("")
        self.username.set("")
        self.password.set("")
        self.access_level.set(0)


    def table_click(self, select_item):
        self.id.set(select_item[0])
        self.name.set(select_item[1])
        self.surname.set(select_item[2])
        self.username.set(select_item[3])
        self.password.set(select_item[4])
        self.access_level.set(select_item[5])

    def save_click(self):
        status, message = EventController.save(
            self.name.get(),
            self.surname.get(),
            self.username.get(),
            self.password.get(),
            self.access_level.get(),
        )
        if status:
            msg.showinfo('Save', message)
            self.reset_from()
        else:
            msg.showerror('Error', message)

    def edit_click(self):
        status, message = EventController.edit(
            self.id.get(),
            self.name.get(),
            self.surname.get(),
            self.username.get(),
            self.password.get(),
            self.access_level.get(),

        )
        if status:
            msg.showinfo('Edit', message)
            self.reset_from()
        else:
            msg.showerror('Error', message)

    def remove_click(self):
        if msg.askyesno("Remove Event", "Are you sure?"):
            status, message = EventController.remove(
                self.id.get())
            if status:
                msg.showinfo('Remove', message)
                self.reset_from()
            else:
                msg.showerror('Error', message)

    def __init__(self):
        win = Tk()
        win.title("Event View")
        win.geometry("800x500")

        self.id = LabelWithEntry(win, "Id", 20, 20, data_type="int", state="readonly")
        self.name = LabelWithEntry(win, "Name", 20, 200, data_type="date")
        self.surname = LabelWithEntry(win, "Surname", 20, 200, data_type="date")
        self.username = LabelWithEntry(win, "Username", 20, 200, data_type="date")
        self.password = LabelWithEntry(win, "Password", 20, 80)
        self.access_level = LabelWithEntry(win, "Access_Level", 20, 150, data_type="int", state="readonly")

        self.table = Table(
            win,["id", "name", "surname", "username", "password", "access_level"],
                           [60, 120, 120, 120, 150, 80, 180, 100], 400, 20, self.table_click
        )
        self.table.refresh_table(EventController.find_all()[1])

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)

        self.reset_from()

        win.mainloop()
