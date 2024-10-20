from datetime import datetime
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.payment_controller import PaymentController
from view.component import LabelWithEntry, Table

class PaymentView:

    def reset_form(self):
        self.id.set(0)
        self.amount.set(0)
        self.date.set("")
        self.payment_type("")
        self.description("")

    @staticmethod
    def table_click(selected_item):
        print(selected_item)

    def save_record(self):
        status, message = PaymentController.save(self.amount.get(), self.date.get(),
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
        status, message = PaymentController.edit(self.id.get(), self.amount.get(), self.date.get(),
                                                 self.payment_type.get(), self.description.get())
        if status:
            msg.showinfo("Edited.", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error!", message)

    def find_record(self):
        status, message = PaymentController.edit(self.id.get(), self.amount.get(), self.date.get(),
                                                 self.payment_type.get(), self.description.get())
        if status:
            msg.showinfo("found.", message)
            self.reset_form()
        else:
            msg.showerror("Not exist", message)






    def __init__(self):
        win = Tk()
        win.geometry("650x400")

        self.id = LabelWithEntry(win, "Id", 20, 100, data_type="int", state= "readonly")
        self.payment_type = LabelWithEntry(win, "Account", 20, 20, data_type= "str")
        self.amount = LabelWithEntry(win, "Amount", 20, 60, data_type= "int")
        self.date = LabelWithEntry(win, "Date", 20, 140, data_type= "datetime", state= "readonly")
        self.description = LabelWithEntry(win, "Description", 20, 180, data_type= "str")

        self.table = Table(win, ["Id", "Amount", "Date","payment Type", "description"],[60, 100, 100, 60, 60], 250, 20, self.table_click)
        self.table.refresh_table(PaymentController.find_all()[1])

        self.table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings")
        self.table.place(x=250, y=20)


        Button(win, text="Save", command=self.save_record).place(x=100, y=220)
        Button(win, text="Remove", command=self.remove_record).place(x=100, y=250)
        Button(win, text="Edit", command=self.edit_record).place(x=100, y=280)
        Button(win, text="Search", command=self.edit_record).place(x=100, y=310)

        self.reset_form()

        win.mainloop()
