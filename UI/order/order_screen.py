# screens/orders_screen.py
import tkinter as tk
from tkinter import ttk
from order.order import order_tab
from order.order_detail import detail_tab
from order.payment_method import payment_tab
from order.table import table_tab

def order_screen(app):
    for widget in app.container.winfo_children():
        widget.destroy()

    frame = tk.Frame(app.container)
    frame.pack(fill="both", expand=True)

    tk.Button(frame, text="⬅",
              font=("Arial", 14),
              command=lambda: app.show_screen("main_menu")).pack(anchor="w", padx=10, pady=10)
    
    notebook = ttk.Notebook(frame)
    notebook.pack(fill="both", expand=True)

    # --- Orders Tab
    order_tab(notebook)
    
    # --- Table Tab
    table_tab(notebook)

    # --- Order Details Tab
    detail_tab(notebook)
    
    # --- Payment Method Tab
    payment_tab(notebook)