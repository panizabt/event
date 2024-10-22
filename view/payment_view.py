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
        self.payment_type.set("")
        self.description.set("")

    @staticmethod
    def table_click(self,selected_item):
        def table_click(self, select_item):
            self.id.set(select_item[0])
            self.amount.set(select_item[1])
            self.date_time.set(select_item[2])
            self.payment_type.set(select_item[3])
            self.description.set(select_item[4])


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
        self.window = Tk()
        self.window.geometry('500x500')
        self.window.title("PAYMENT")

        self.id = LabelWithEntry(self.window, "Id", 20, 100, data_type="int", state= "readonly")
        self.amount = LabelWithEntry(self.window, "Amount", 20, 60, data_type= "int")
        self.date = LabelWithEntry(self.window, "Date", 20, 140, data_type= "datetime", satat= "readonly")
        self.payment_type = LabelWithEntry(self.window, "payment_type", 20, 20, data_type="str")
        self.description = LabelWithEntry(self.window, "Description", 20, 180, data_type= "str")

        self.table = Table(self.window, ["Id", "Amount", "Date","payment Type", "description"],[60, 100, 100, 60, 60], 250, 20 ,self.table_click )
        self.table.refresh_table(PaymentController.find_all()[1])

        self.table = ttk.Treeview(self.window, columns=(1, 2, 3, 4, 5), show="headings")
        self.table.place(x=250, y=20)


        Button(self.window, text="Save", command=self.save_record).place(x=100, y=220)
        Button(self.window, text="Remove", command=self.remove_record).place(x=100, y=250)
        Button(self.window, text="Edit", command=self.edit_record).place(x=100, y=280)
        Button(self.window, text="Search", command=self.find_record).place(x=100, y=310)

        self.reset_form()

        self.window.mainloop()


ui=PaymentView()
