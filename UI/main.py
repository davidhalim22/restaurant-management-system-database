import tkinter as tk
from tkinter import ttk
from customer import create_customer_tab
from staff import create_staff_tab
from menu import create_menu_tab


# MAIN TKINTER WINDOW
root = tk.Tk()
root.title("Restaurant Management System")
root.geometry("1280x720")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

create_customer_tab(notebook)
create_staff_tab(notebook)
create_menu_tab(notebook)

# RUN TKINTER
root.mainloop()