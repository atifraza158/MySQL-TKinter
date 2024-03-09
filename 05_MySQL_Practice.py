import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
import mysql.connector as mysql

global main_frame

def menu_frame(parent):
    menu_frame = ctk.CTkFrame(parent)
    menu_frame.place(x = 0, y = 0, relwidth = 0.2, relheight = 1)

    # label1 = ctk.CTkLabel(menu_frame, bg_color='lightgreen')
    # label1.pack(expand = True, fill = 'both')

    menu_frame.columnconfigure((0,1), weight=1, uniform='a')
    menu_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1, uniform='a')

    home_button = ctk.CTkButton(menu_frame, text="Home", bg_color='transparent', fg_color='transparent', hover_color='grey', command=lambda: switch_pages(home_page))
    about_button = ctk.CTkButton(menu_frame, text="About", bg_color='transparent', fg_color='transparent', hover_color='grey', command=lambda: switch_pages(about_page))
    contact_button = ctk.CTkButton(menu_frame, text="Contact", bg_color='transparent', fg_color='transparent', hover_color='grey', command=lambda: switch_pages(contact_page))

    other_button1 = ctk.CTkButton(menu_frame, text="Other 1", bg_color='transparent', fg_color='transparent', hover_color='grey')
    other_button2 = ctk.CTkButton(menu_frame, text="Other 2", bg_color='transparent', fg_color='transparent', hover_color='grey')
    other_button3 = ctk.CTkButton(menu_frame, text="Other 3", bg_color='transparent', fg_color='transparent', hover_color='grey')

    home_button.grid(row = 1, column = 0, columnspan = 2, padx = 8, sticky = 'nsew')
    about_button.grid(row = 2, column = 0, columnspan = 2, padx = 8, sticky = 'nsew')
    contact_button.grid(row = 3, column = 0, columnspan = 2, padx = 8, sticky = 'nsew')

    other_button1.grid(row = 4, column = 0, columnspan = 2, padx = 8, sticky = 'nsew')
    other_button2.grid(row = 5, column = 0, columnspan = 2, padx = 8, sticky = 'nsew')
    other_button3.grid(row = 6, column = 0, columnspan = 2, padx = 8, sticky = 'nsew')

    return menu_frame

def main_frame_func(parent):
    global main_frame
    main_frame = ctk.CTkFrame(parent)
    main_frame.place(relx = 0.2, y = 0, relwidth = 0.8, relheight = 1)
    return main_frame

def home_page(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    home_frame = ctk.CTkFrame(parent)
    home_frame.pack(expand = True, fill = 'both')

    label3 = ctk.CTkLabel(home_frame, text="Home Page", bg_color='lightgreen')
    label3.pack(expand = True, fill = 'both')
    label3.configure(font = ('arial', 20))
    # return home_frame

def about_page(parent):
    for widget in parent.winfo_children():
        widget.destroy()
    home_frame = ctk.CTkFrame(parent)
    home_frame.pack(expand = True, fill = 'both')

    label3 = ctk.CTkLabel(home_frame, text="About Page", bg_color='pink')
    label3.pack(expand = True, fill = 'both')
    label3.configure(font = ('arial', 20))
    return home_frame

def contact_page(parent):
    for widget in parent.winfo_children():
        widget.destroy()
    home_frame = ctk.CTkFrame(parent)
    home_frame.pack(expand = True, fill = 'both')

    label3 = ctk.CTkLabel(home_frame, text="Contact Page", bg_color='crimson')
    label3.pack(expand = True, fill = 'both')
    label3.configure(font = ('arial', 20))
    return home_frame

def switch_pages(page):
    global main_frame
    if main_frame:
        page(main_frame)

window = ctk.CTk()
window.title("MySQL")
window.geometry('700x400')
window.minsize(700, 400)

menu_frame(window)
main_frame_func(window)



window.mainloop()