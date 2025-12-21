import tkinter as tk
from tkinter import ttk
from customer.customer import customer_tab
from customer.membership import membership_tab

from customer.reservation import reservation_tab

def customer_screen(app):
    for widget in app.container.winfo_children():
        widget.destroy()

    frame = tk.Frame(app.container)
    frame.pack(fill="both", expand=True)

    tk.Button(frame, text="⬅",
              font=("Arial", 14),
              command=lambda: app.show_screen("main_menu")).pack(anchor="w", padx=10, pady=10)
    
    notebook = ttk.Notebook(frame)
    notebook.pack(fill="both", expand=True)

    # --- Customers Tab
    customer_tab(notebook)

    # --- Membership Tab
    membership_tab(notebook)
    
    # --- reservation Tab
    reservation_tab(notebook)