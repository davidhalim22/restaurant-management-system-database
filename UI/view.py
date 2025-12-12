import tkinter as tk
from tkinter import ttk, messagebox
from utils import refresh_table, open_insert_window, update_window, delete_rows
from database import connect_db


def view_screen(app):
    for widget in app.container.winfo_children():
        widget.destroy()

    frame = tk.Frame(app.container)
    frame.pack(fill="both", expand=True)

    tk.Button(frame, text="⬅",
              font=("Arial", 14),
              command=lambda: app.show_screen("main_menu")).pack(anchor="w", padx=10, pady=10)
    
    notebook = ttk.Notebook(frame)
    notebook.pack(fill="both", expand=True)