from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.event_controller import EventController
from model.entity import Event
from view.component import LabelWithEntry, Table


class EventView:
    def reset_from(self):
        self.id.set(0)
        self.title.set("")
        self.start_date_time.set("")
        self.end_date_time.set("")
        self.event_type.set("")
        self.duration.set(0)
        self.description.set("")
        self.price.set(0)
        self.salon_id.set(0)
        self.clear_table()
        self.show_on_table()

    def table_click(self, select_item):
        event = Event(*select_item)
        self.id.set(event.id)
        self.title.set(event.title)
        self.start_date_time.set(event.start_date_time)
        self.end_date_time.set(event.end_date_time)
        self.event_type.set(event.event_type)
        self.duration.set(event.duration)
        self.description.set(event.description)
        self.price.set(event.price)
        self.salon_id.set(event.salon_id)

    def save_click(self):
        status, message = EventController.save(
            self.title.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.event_type.get(),
            self.duration.get(),
            self.description.get(),
            self.price.get(),
            self.salon_id.get(),
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_from()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = EventController.edit(
            self.id.get(),
            self.title.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.event_type.get(),
            self.duration.get(),
            self.description.get(),
            self.price.get(),
            self.salon_id.get(),

        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_from()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        if msg.askyesno("Remove Event", "Are you sure?"):
            status, message = EventController.remove(
                self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_from()
            else:
                msg.showerror("Remove Error", message)

    def clear_table(self):
       self.table.delete(*self.table.get_children())

    def show_on_table(self):
       events = EventController.find_all()[1]
       for event in events:
           self.table.insert("", "end", values=event)


    def __init__(self):
        win = Tk()
        win.title("Event View")
        win.geometry("1200x500")

        self.id = LabelWithEntry(win, "Id", 20, 30, data_type="int", state="readonly")
        self.title = LabelWithEntry(win, "Title", 20, 60)
        self.start_date_time = LabelWithEntry(win, "Start_date_time", 20, 100)
        self.end_date_time = LabelWithEntry(win, "End_date_time", 20, 100)
        self.event_type = LabelWithEntry(win, "Event_type", 20, 80)
        self.duration = LabelWithEntry(win, "Duration", 20, 150, data_type="int")
        self.description = LabelWithEntry(win, "Description", 20, 200)
        self.price = LabelWithEntry(win, "Price", 20, 230, data_type="int")
        self.salon_id = LabelWithEntry(win, "Salon", 20, 250, data_type="int")

        self.table = Table(win,
                           ["Id", "Title", "Start_date_time", "End_date_time", "Event_type", "Duration", "Description",
                            "Price", "Salon_id"], [60, 100, 120, 120, 100, 80, 80, 100, 100], 400, 20,
                           self.table_click)
        self.show_on_table()

        Button(win, text="Save", width=10, bg="red", command=self.save_click).place(x=100, y=380)
        Button(win, text="Edit", width=10, bg="blue", command=self.edit_click).place(x=100, y=310)
        Button(win, text="Remove", width=10, bg="pink", command=self.remove_click).place(x=100, y=340)


        self.reset_form()

        win.mainloop()


ui = EventView()




