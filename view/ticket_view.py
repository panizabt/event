from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.ticket_controller import TicketController
from view.component import LabelWithEntry, Table


class TicketView:
    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.start_date.set("")
        self.duration.set(0)
        self.event.set("")
        self.price.set(0)
        self.payment.set("")
        self.customer_id.set(0)
        self.clear_table()
        self.show_on_table()

    @staticmethod
    def table_click(self, selected_item):
        self.id.set(selected_item[0])
        self.title.set(selected_item[1])
        self.start_date.set(selected_item[2])
        self.duration.set(selected_item[3])
        self.event.set(selected_item[4])
        self.price.set(selected_item[5])
        self.payment.set(selected_item[6])
        self.customer_id.set(selected_item[7])

    def save_click(self):
        status, message = TicketController.save(
            self.title.get(),
            self.start_date.get(),
            self.duration.get(),
            self.event.get(),
            self.price.get(),
            self.payment.get(),
            self.customer_id.get(),
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = TicketController.edit(
            self.id.get(),
            self.title.get(),
            self.start_date.get(),
            self.duration.get(),
            self.event.get(),
            self.price.get(),
            self.payment.get(),
            self.customer_id.get(),
        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        if msg.askyesno("Remove Ticket", "Are you sure?"):
            status, message = TicketController.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)

    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def show_on_table(self):
        tickets = TicketController.find_all()[1]
        for ticket in tickets:
            self.table.insert("", "end", values=ticket)

    def __init__(self):
        win = Tk()
        win.title("Ticket Management System")
        win.geometry("1200x500")

        self.id = LabelWithEntry(win, "ID", 20, 30, data_type="int", state="readonly")
        self.title = LabelWithEntry(win, "Title", 20, 60)
        self.start_date = LabelWithEntry(win, "Start Date", 20, 100)
        self.duration = LabelWithEntry(win, "Duration", 20, 140, data_type="int")
        self.event = LabelWithEntry(win, "Event", 20, 180)
        self.price = LabelWithEntry(win, "Price", 20, 220, data_type="int")
        self.payment = LabelWithEntry(win, "Payment", 20, 260)
        self.customer_id = LabelWithEntry(win, "Customer ID", 20, 300, data_type="int")

        self.table = Table(win, ["ID", "Title", "Start Date", "Duration", "Event", "Price", "Payment", "Customer ID"],
          [60, 100, 120, 80, 100, 60, 80, 100], 400, 20, self.table_click)
        self.show_on_table()

        Button(win, text="Save", width=10, bg="green", command=self.save_click).place(x=100, y=340)
        Button(win, text="Edit", width=10, bg="yellow", command=self.edit_click).place(x=100, y=380)
        Button(win, text="Remove", width=10, bg="red", command=self.remove_click).place(x=100, y=420)

        # self.reset_form()

        win.mainloop()


ui = TicketView()
