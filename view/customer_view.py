import tkinter
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.customer_controller import CustomerController
#from controller import customer_controller as CustomerController
from view.component import LabelWithEntry, Table


class CustomerView:
    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.username.set("")
        self.password.set("")
        self.address.set("")
        self.phone.set("")
        self.postal_code.set("")
        #self.clear_table()
        #self.show_on_table()

    @staticmethod
    def table_click(self, select_item):

         self.id.set(select_item[0])
         self.name.set(select_item[1])
         self.family.set(select_item[2])
         self.password.set(select_item[3])
         self.address.set(select_item[4])
         self.phone.set(select_item[5])
         self.postal_code.set(select_item[6])


    def save_click(self):
        status, message = CustomerController.save(
            self.name.get(),
            self.family.get(),
            self.username.get(),
            self.password.get(),
            self.address.get(),
            self.phone.get(),
            self.postal_code.get()
        )
        if status:
            msg.showinfo("Save","customer save shood")
            self.reset_form()
        else:
            msg.showerror("Save Error","custome save naaashod")



    def edit_click(self):
        status, message =CustomerController.edit(
            self.name.get(),
            self.family.get(),
            self.username.get(),
            self.password.get(),
            self.address.get(),
            self.phone.get(),
            self.postal_code.get()
        )
        if status:
            msg.showinfo("Edit", "customer edit shood")
            self.reset_form()
        else:
            msg.showerror("edit Error","customer edit naaashod")



    def remove_click(self):
        if msg.askyesno("Remove person","Are you sure ?"):
            status, message =CustomerController.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)


    def clear_table(self):
        self.table.delete(*self.table.get_children())


    def show_on_table(self):
        customer = CustomerController.find_all()[1]
        for customer in customer:
            self.table.insert("", "end", values=customer)



    def __init__(self):
        self.window =Tk()
        self.window.geometry('1200x500')
        self.window.title("Customer")


        self.id = LabelWithEntry(self.window, "ID", 50, 20, data_type="int", state="readonly")
        self.title = LabelWithEntry(self.window, "name", 50, 60)
        self.week_day = LabelWithEntry(self.window, "family", 50, 100)
        self.start_time= LabelWithEntry(self.window, "username", 50, 140)
        self.start_date= LabelWithEntry(self.window,"phone", 50, 180)
        self.end_time= LabelWithEntry(self.window, "postal_code", 50, 220)
        self.end_time = LabelWithEntry(self.window, "password", 50, 260)
        self.end_time = LabelWithEntry(self.window, "address", 50, 290)



        # self.table = Table(self.window, ["ID", "name", "family", "username","phone","postal_code ", "password"," address"],
        #                    [60, 100, 100, 80, 80], 250, 20,self.table_click)
        # self.show_on_table()
        # self.table.refresh_table(CustomerController.find_all()[1])

        self.table = Table(self.window , ["ID", "name", "family", "username", "phone", "postal_code"],
                           [120, 120, 120, 120, 120, 120, 120, 120], 400, 20, self.table_click)
        self.show_on_table()


        Button(self.window, text="Save", width=10,bg="green" ,fg="black", command=self.save_click).place(x=130, y=320)
        Button(self.window, text="Edit", width=10,bg="yellow" ,fg="black",  command=self.edit_click).place(x=130, y=360)
        Button(self.window, text="Remove", width=10,bg="red" , fg="black", command=self.remove_click).place(x=130, y=400)

#        self.reset_form()
        self.window.mainloop()

ui = CustomerView()

