from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.event_controller import EventController
from view.component import LabelWithEntry, Table


class EventView:
    def reset_from(self):
        self.id.set(0)
        self.title_date.set("")
        self.start_time.set("")
        self.end_date_time.set("")
        self.title_type.set("")
        self.duration.set(0)
        self.description.set("")
        self.price.set(0)


    def table_click(self, select_item):
         self.id.set(select_item[0])
         self.title_date.set(select_item[1])
         self.start_date.set(select_item[2])
         self.end_date_time.set(select_item[3])
         self.title_type.set(select_item[4])
         self.duration.set(select_item[5])
         self.description.set(select_item[6])
         self.price.set(select_item[7])


    def save_click(self):
         status, message = EventController.save(
             self.title_date.get(),
             self.start_date.get(),
             self.end_date_time.get(),
             self.title_type.get(),
             self.duration.get(),
             self.description.get(),
             self.price.get(),
         )
         if status:
             msg.showinfo('Save', message)
             self.reset_from()
         else:
             msg.showerror('Error', message)

    def edit_click(self):
         status, message = EventController.edit(
             self.id.get(),
             self.title_date.get(),
             self.start_date.get(),
             self.end_date_time.get(),
             self.title_type.get(),
             self.duration.get(),
             self.description.get(),
             self.price.get(),

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

        self.id = LabelWithEntry(win,"Id", 20, 20, data_type="int", state="readonly")
        self.title_date = LabelWithEntry(win, "Title Date", 20, 200, data_type="date")
        self.start_date = LabelWithEntry(win, "Start Date", 20, 200, data_type="date")
        self.end_date_date = LabelWithEntry(win, "End Date Date", 20, 200, data_type="date")
        self.title_type = LabelWithEntry(win, "Title Type", 20, 80)
        self.duration = LabelWithEntry(win, "Duration", 20, 150, data_type="int")
        self.description = LabelWithEntry(win, "Description", 20, 200)
        self.price = LabelWithEntry(win, "Price", 20, 200, data_type="int")

        self.table = Table(win, ["id", "title_date", "start_date", "end_date_time", "title_type", "duration", "description", "price"], [60, 120, 120, 120, 150, 80, 180, 100], 400, 20, self.table_click)
        self.table.refresh_table(EventController.find_all()[1])
    
        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)

        self.reset_form()

        win.mainloop()




