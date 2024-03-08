import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
import sqlite3

window = ttk.Window(themename='journal')
window.title("SQLITE Integeration")

# Database
# Create Submit Function
def submit():
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)''',
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                })

    cursor.close()
    connection.commit()
    connection.close()

    # Clear text boxes
    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    address.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zipcode.delete(0, tk.END)


def query():
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM addresses")
    results = cursor.fetchall()
    print(results)
    # cursor.fetchmany()
    # cursor.fetchone()

    connection.commit()
    connection.close()


f_name = ttk.Entry(window)
f_name.grid(row = 0, column=1, padx=20)
l_name = ttk.Entry(window)
l_name.grid(row = 1, column=1)
address = ttk.Entry(window)
address.grid(row = 2, column=1)
city = ttk.Entry(window)
city.grid(row = 3, column=1)
state = ttk.Entry(window)
state.grid(row = 4, column=1)
zipcode = ttk.Entry(window)
zipcode.grid(row = 5, column=1)

f_name_label = ttk.Label(window, text="First Name")
f_name_label.grid(row = 0, column=0,)

l_name_label = ttk.Label(window, text='Last Name')
l_name_label.grid(row = 1, column=0)

address_label = ttk.Label(window, text='Address')
address_label.grid(row = 2, column=0)

city_label = ttk.Label(window, text='City')
city_label.grid(row = 3, column=0)

state_label = ttk.Label(window, text='State')
state_label.grid(row = 4, column=0)

zipcode_label = ttk.Label(window, text='Zip Code')
zipcode_label.grid(row = 5, column=0)

# Create Submit Button
submit_button = ttk.Button(window, text='Add Records to Database', command=submit)
submit_button.grid(row = 6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create Query Button
query_button = ttk.Button(window, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)


window.mainloop()