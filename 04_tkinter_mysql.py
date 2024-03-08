import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
# import customtkinter as ctk
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import customtkinter as ctk
import mysql.connector as mysql



# ------------------------ All Methods Here --------------------------
# Save Data
def insert_data():
    global name_field, phone_field, email_field
    name = name_field.get()
    phone = str(phone_field.get())
    email = email_field.get()

    if name == '' or phone == '' or email == '':
        showinfo("Insertion Warning", "Please fill all fields")
    else :
        connection = mysql.connect(host = "localhost", user = "root", password = "", database = "tkinter_mysql")
        cursor = connection.cursor()
        # cursor.execute("INSERT INTO student_data ('" + name + "', '" + phone + "', '" + email + "')")
        cursor.execute("INSERT INTO student_data (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
        cursor.execute("commit")
        
        showinfo("Insert Status", "Data inserted Successfully")
        connection.close()

        name_field.delete(0, tk.END)
        phone_field.delete(0, tk.END)
        email_field.delete(0, tk.END)
        display_data()

# Delete Data
def delete_data():
    id = id_field.get()
    if id_field.get() == '':
        showinfo("Deletion Warning", "Please fill id field to delete data")
    else :
        connection = mysql.connect(host = "localhost", user = "root", password = "", database = "tkinter_mysql")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM student_data WHERE id = %s", (id,))
        cursor.execute("commit")
        
        showinfo("Delete Status", "Data deleted Successfully")
        connection.close()
        id_field.delete(0, tk.END)
        display_data()

# Update Data
def update_data():
    global name_field, phone_field, email_field
    name = name_field.get()
    phone = str(phone_field.get())
    email = email_field.get()
    id = id_field.get()
    if id_field.get() == '':
        showinfo("Update Status", "No Field should be empty")
    else :
        connection = mysql.connect(host = "localhost", user = "root", password = "", database = "tkinter_mysql")
        cursor = connection.cursor()
        cursor.execute("UPDATE student_data SET name = '"+ name + "', phone = '"+ phone + "', email = '"+ email + "' WHERE id = '"+ str(id) +"'")
        cursor.execute("commit")
        
        showinfo("Update Status", "Data Updated Successfully")
        connection.close()
        name_field.delete(0, tk.END)
        phone_field.delete(0, tk.END)
        email_field.delete(0, tk.END)
        id_field.delete(0, tk.END)
        display_data()

# Read Data
def read_data():
    id = id_field.get()
    if id_field.get() == '':
        showinfo("Read Status", "Please fill id field to get data")
    else :
        connection = mysql.connect(host = "localhost", user = "root", password = "", database = "tkinter_mysql")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student_data WHERE id = %s", (id,))
        rows = cursor.fetchall()

        for row in rows:
            name_field.insert(tk.END, row[1])
            phone_field.insert(tk.END, row[2])
            email_field.insert(tk.END, row[3])
        cursor.execute("commit")
        
        connection.close()

# Insert in Table
def display_data():
    connection = mysql.connect(host = "localhost", user = "root", password = "", database = "tkinter_mysql")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student_data")
    rows = cursor.fetchall()

    for row in table.get_children():
        table.delete(row)

    for row in rows:
        table.insert(parent='', index=tk.END, values=row)


# -------------------------- Statrng Here ----------------------------
window = ttk.Window(themename='solar')
window.title("Students")
window.geometry('1300x700')

main_frame = ttk.Frame(window)
menu_frame = ttk.Frame(window)


main_frame.place(relx=0.4, y = 0, relwidth=0.7, relheight=1,)
menu_frame.place(x = 0, y = 0, relwidth = 0.4, relheight = 1)

# Menu Frame Layout
menu_frame.columnconfigure((0,1), weight=1, uniform='a')
menu_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1, uniform='a')

# All Labels Used
name_label = ctk.CTkLabel(menu_frame, text="Name: ")
phone_label = ctk.CTkLabel(menu_frame, text="Phone No: ")
email_label = ctk.CTkLabel(menu_frame, text="Email: ")
id_label = ctk.CTkLabel(menu_frame, text="ID: ")

# Entry Fields Used
name_field = ctk.CTkEntry(menu_frame, placeholder_text="Enter Name here", corner_radius=4)
phone_field = ctk.CTkEntry(menu_frame, placeholder_text="Enter Phone number", corner_radius=4)
email_field = ctk.CTkEntry(menu_frame, placeholder_text="Enter Email address", corner_radius=4)
id_field = ctk.CTkEntry(menu_frame, placeholder_text="Enter ID to delete", corner_radius=4)

# Buttons Used
save_button = ctk.CTkButton(menu_frame, text="Save Data", corner_radius=2, command=insert_data)
delete_button = ctk.CTkButton(menu_frame, text="Delete Data", corner_radius=2, command=delete_data)
update_button = ctk.CTkButton(menu_frame, text="Update Data", corner_radius=2, command=update_data)
read_button = ctk.CTkButton(menu_frame, text="Read Data", corner_radius=2, command=read_data)


# Layout Building
name_label.grid(row = 0, column=0, padx=10, sticky = 'w')
name_field.grid(row = 0, column=1, padx=10, sticky = 'ew')

phone_label.grid(row = 1, column=0, padx=10, sticky = 'w')
phone_field.grid(row = 1, column=1, padx=10, sticky = 'ew')

email_label.grid(row = 2, column=0, padx=10, sticky = 'w')
email_field.grid(row = 2, column=1, padx=10, sticky = 'ew')

id_label.grid(row = 3, column=0, padx=10, sticky = 'w')
id_field.grid(row = 3, column=1, padx=10, sticky = 'ew')

save_button.grid(row = 4, column = 0, columnspan=2, sticky = 'e', padx =10)
delete_button.grid(row = 4, column = 0, columnspan=2, sticky = 'e', padx =160)
update_button.grid(row = 4, column = 0, columnspan=2, sticky = 'w', padx = 10)
read_button.grid(row = 5, column = 0, columnspan=2, sticky = 'nsew', padx = 10)

# Table Creation
table = ttk.Treeview(main_frame, columns=('id', 'fname', 'lname', 'address'), show='headings')
table.heading('id', text="id",)
table.heading('fname', text="First Name",)
table.heading('lname', text="Last Name",)
table.heading('address', text="Address",)

table.pack(expand=True, fill='both')

display_data()
window.mainloop()