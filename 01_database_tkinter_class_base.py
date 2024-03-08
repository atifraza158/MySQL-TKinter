import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
import sqlite3

class App(ttk.Window):
    def __init__(self, title, screen_size):
        super().__init__(themename='solar')

        # Basic WIndow Setup
        self.title(title)
        self.geometry(f"{screen_size[0]}x{screen_size[1]}")

        # Layout Building
        self.menu = MainFrame(self)
        self.table = DataDisplay(self)
        self.mainloop()
        

# Building main UI
class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(side='left', expand=True, fill='both')
        self.create_component()
        
    # Widgets Creating on Window
    def create_component(self):
        f_name_label = ttk.Label(self, text="First Name")
        f_name_label.pack()
        self.f_name = ttk.Entry(self)
        self.f_name.pack()

        l_name_label = ttk.Label(self, text='Last Name')
        l_name_label.pack()
        self.l_name = ttk.Entry(self)
        self.l_name.pack()


        address_label = ttk.Label(self, text='Address')
        address_label.pack()
        self.address = ttk.Entry(self)
        self.address.pack()

        submit_button = ttk.Button(self, text='Add Records to Database', command=self.create_connection)
        submit_button.pack(pady=20)

        query_button = ttk.Button(self, text='Show Records', command=self.query_data)
        query_button.pack()
    
    # Just check if everything is working
    def submit(self):
        # Access the Entry widgets' text using self
        f_name_text = self.f_name.get()
        l_name_text = self.l_name.get()
        address_text = self.address.get()
        # Implement the logic to handle submission, for example:
        print(f"First Name: {f_name_text}, Last Name: {l_name_text}, Address: {address_text}")

        # Optionally, clear the entries after submitting
        self.f_name.delete(0, tk.END)
        self.l_name.delete(0, tk.END)
        self.address.delete(0, tk.END)
    
    # Creating Connection
    def create_connection(self):
        connection = sqlite3.connect("My_DB.db")
        command = '''CREATE TABLE IF NOT EXISTS addresses (f_name TEXT, l_name TEXT, address TEXT)'''

        connection.execute(command)
        cursor = connection.cursor()

        insert_data_command = '''INSERT INTO addresses (f_name, l_name, address) VALUES (?,?,?)'''
        insert_data_tuple = (self.f_name.get(), self.l_name.get(), self.address.get())

        cursor.execute(insert_data_command, insert_data_tuple)
        connection.commit()
        connection.close()

        self.f_name.delete(0, tk.END)
        self.l_name.delete(0, tk.END)
        self.address.delete(0, tk.END)
    
    def query_data(self):
        connection = sqlite3.connect("My_DB.db")
        cursor = connection.cursor()

        cursor.execute("SELECT *, oid FROM addresses")
        results = cursor.fetchall()

        print(results)
        print_records = ''

        for record in results:
            print_records += str(record) + "\n"

        query_label = ttk.Label(self, text=print_records)
        query_label.pack()
        connection.commit()
        connection.close()


class DataDisplay(ttk.Frame):
        def __init__(self, parent):
            super().__init__(master=parent)
            self.pack(side='left', expand=True, fill='both')
            self.create_table()

        def create_table(self):
            table = ttk.Treeview(self, columns=('1', '2', '3'), show='headings')
            table.heading('1', text="First Name")
            table.heading('2', text="Last Name")
            table.heading('3', text="Address")
            table.pack(fill='both', expand=True)

# Creating Main Window
App("Hello", (700, 400))