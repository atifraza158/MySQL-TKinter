import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
# import customtkinter as ctk
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import sqlite3
import customtkinter as ctk

# Inserting data into database
def save_data():
    fname = f_name.get()
    lname = l_name.get()
    address = address_entry.get()
    if fname == '' or lname == '' or address == '':
        showinfo("Insert Status", "All Fields are required")
    else:
        connection = sqlite3.connect("My_DB.db")
        cursor = connection.cursor()

        command = '''CREATE TABLE IF NOT EXISTS addresses(
        name TEXT,
        email TEXT,
        password TEXT
        )'''

        insert_data = '''INSERT INTO addresses (
        f_name,
        l_name,
        address
        ) 
        VALUES (?, ?, ?)'''

        insert_data_tuple = (fname, lname, address)

        cursor.execute(insert_data, insert_data_tuple)

        cursor.execute(command)
        connection.commit()
        cursor.close()

        toast = ToastNotification(
        title="SQLITE Message",
        message="Data inserted successfully",
        duration=3000,
        )
        toast.show_toast()
        fetch_data()
        display_data()

# Fetching data from database
def fetch_data():
    connection = sqlite3.connect("My_DB.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM addresses')
    results = cursor.fetchall()
    print(results)

# Delete Records
def delete_data():
    if delete_id.get() == "":
        showinfo("Delete Status", "Please insert id no.")
    else:
        connection = sqlite3.connect("My_DB.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM addresses WHERE oid = " + delete_id.get())

        cursor.execute("SELECT oid, * FROM addresses")
        rows = cursor.fetchall()

        delete_id.delete(0, tk.END)
        for row in table.get_children():
            table.delete(row)
        
        for row in rows:
            table.insert(parent='', index=tk.END, values=row)

        connection.commit()
        connection.close()
# Display Data
def display_data():
    connection = sqlite3.connect("My_DB.db")
    cursor = connection.cursor()

    cursor.execute("SELECT oid, * FROM addresses")
    rows = cursor.fetchall()
    connection.close()

    for row in table.get_children():
        table.delete(row)
    
    for row in rows:
        table.insert(parent='', index=tk.END, values=row)

# Update Records

def update_data():
    connection = sqlite3.connect("My_DB.db")
    cursor = connection.cursor()

    cursor.execute()

    connection.commit()
    connection.close()
# Main Window
window = ttk.Window(themename='solar')
window.title("Students")
window.geometry('1300x700')

main_frame = ttk.Frame(window)
menu_frame = ttk.Frame(window)

# label1 = ttk.Label(main_frame, background='lightgreen')
# label1.pack(expand = True, fill = 'both')

# label1 = ctk.CTkLabel(menu_frame, bg_color='pink')
# label1.pack(expand = True, fill = 'both')

main_frame.place(relx=0.4, y = 0, relwidth=0.7, relheight=1,)
menu_frame.place(x = 0, y = 0, relwidth = 0.4, relheight = 1)


f_name_label = ttk.Label(menu_frame, text="First Name")
f_name_label.pack()
f_name = ttk.Entry(menu_frame)
f_name.pack(fill='x', padx=50)

l_name_label = ttk.Label(menu_frame, text='Last Name')
l_name_label.pack()
l_name = ttk.Entry(menu_frame)
l_name.pack(fill='x', padx=50)


address_label = ttk.Label(menu_frame, text='Address')
address_label.pack()
address_entry = ttk.Entry(menu_frame,)
address_entry.pack(fill='x', padx=50)

submit_button = ttk.Button(menu_frame, text='Add Records', command=save_data)
submit_button.pack(pady=10, fill='x', padx=50)

delete_id_label = ttk.Label(menu_frame, text='Insert ID of Record to Delete')
delete_id_label.pack(pady=10)

delete_id = ctk.CTkEntry(menu_frame, placeholder_text='Enter ID', corner_radius=0)
delete_id.pack(fill='x', padx=50)

delete_button = ttk.Button(menu_frame, text='Delete Records', command=delete_data)
delete_button.pack( fill='x', padx=50)

# Table Creation
table = ttk.Treeview(main_frame, columns=('id', 'fname', 'lname', 'address'), show='headings')
table.heading('id', text="id",)
table.heading('fname', text="First Name",)
table.heading('lname', text="Last Name",)
table.heading('address', text="Address",)

table.pack(expand=True, fill='both')


display_data()
window.mainloop()