from datetime import datetime
from tkinter import *
# import tkinter.ttk as ttk
import tkinter.messagebox as msg
from model.entity import Payment
from controller.payment_controller import PaymentController
from view.component import LabelWithEntry, Table

class PaymentView:

    def reset_form(self):
        self.id.set(0)
        self.amount.set(0)
        self.date_time.set("")
        self.payment_type.set("")
        self.description.set("")


    def table_click(self,selected_item):
        payment = Payment(*selected_item)
        self.id.set(payment.id)
        self.amount.set(payment.amount)
        self.date_time.set(payment.date_time)
        self.payment_type.set(payment.payment_type)
        self.description.set(payment.description)




    def save_record(self):
        status, message = PaymentController.save(self.amount.get(), self.date_time.get(),
                                                 self.payment_type.get(), self.description.get())
        if status:
            msg.showinfo("Saved.", message)
            self.reset_form()
        else:
            msg.showerror("Save Error!", message)



    def remove_record(self):
        if msg.askyesno("Remove Payment!", "Are you sure?"):
            status, message = PaymentController.remove(self.id.get())
            if status:
                msg.showinfo("Removed.", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error!", message)



    def edit_record(self):
        status, message = PaymentController.edit(self.id.get(), self.amount.get(), self.date_time.get(),
                                                 self.payment_type.get(), self.description.get())
        if status:
            msg.showinfo("Edited.", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error!", message)



    def find_record(self):
        status, message = PaymentController.edit(self.id.get(), self.amount.get(), self.date_time.get(),
                                                 self.payment_type.get(), self.description.get())
        if status:
            msg.showinfo("found.", message)
            self.reset_form()
        else:
            msg.showerror("Not exist", message)


    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def show_on_table(self):
        tickets = PaymentController.find_all()[1]
        for payment in tickets:
            self.table.insert("", "end", values=payment)



    def __init__(self):
        win = Tk()
        win.geometry("900x450")
        win.title("Pament Management")

        self.id = LabelWithEntry(win, "Id", 40 , 30, data_type="int", state="readonly")
        self.amount = LabelWithEntry(win, "Amount", 40, 60, data_type="int")
        self.date_time = LabelWithEntry(win, "Date_time", 40, 80)
        self.payment_type = LabelWithEntry(win, "PaymentType", 40, 100, data_type="str")
        self.description = LabelWithEntry(win, "Description", 40, 120, data_type="str")

        self.table = Table(win, ["Id", "Amount", "Date","payment Type", "description"],[60, 100, 100, 120, 150], 350, 50 ,self.table_click )
        self.table.refresh_table(PaymentController.find_all()[1])

        self.show_on_table()
        # self.table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings")
        # self.table.place(x=250, y=20)


        Button(win, text="Save", width=10, bg="green", command=self.save_record).place(x=100, y=220)
        Button(win, text="Remove", width=10, bg="yellow", command=self.remove_record).place(x=100, y=250)
        Button(win, text="Edit", width=10, bg="red", command=self.edit_record).place(x=100, y=280)
        Button(win, text="Search", width=10, bg="blue", command=self.find_record).place(x=100, y=310)


        # self.reset_form()

        win.mainloop()


ui = PaymentView()
