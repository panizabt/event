from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.ticket_controller import TicketController
from model.entity import Ticket
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


    def table_click(self, selected_item):
        ticket = Ticket(*selected_item)
        self.id.set(ticket.id)
        self.title.set(ticket.title)
        self.start_date.set(ticket.start_date_time)
        self.duration.set(ticket.duration)
        self.event_id.set(ticket._event_id)
        self.price.set(ticket.price)
        self.payment_id.set(ticket._payment_id)
        self.customer_id.set(ticket._customer_id)

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
        win.geometry("1150x450")

        self.id = LabelWithEntry(win, "ID", 20, 30, data_type="int", state="readonly")
        self.title = LabelWithEntry(win, "Title", 20, 60)
        self.start_date = LabelWithEntry(win, "Start Date", 20, 100)
        self.duration = LabelWithEntry(win, "Duration", 20, 140, data_type="int")
        self.event_id = LabelWithEntry(win, "Event ID", 20, 180, data_type="int")
        self.price = LabelWithEntry(win, "Price", 20, 220, data_type="int")
        self.payment_id = LabelWithEntry(win, "Payment ID", 20, 260, data_type="int")
        self.customer_id = LabelWithEntry(win, "Customer ID", 20, 300, data_type="int")

        self.table = Table(win, ["ID", "Title", "Start Date", "Duration", "Event ID", "Price", "Payment ID", "Customer ID"],
          [60, 100, 120, 80, 100, 60, 80, 100], 400, 20, self.table_click)
        self.show_on_table()

        Button(win, text="Save", width=10, bg="green", command=self.save_click).place(x=90, y=350)
        Button(win, text="Edit", width=10, bg="yellow", command=self.edit_click).place(x=190, y=350)
        Button(win, text="Remove", width=10, bg="red", command=self.remove_click).place(x=290, y=350)

        # self.reset_form()

        win.mainloop()

ui = TicketView()

