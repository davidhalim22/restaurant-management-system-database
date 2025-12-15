import tkinter as tk
from tkinter import ttk
from menu.menu import menu_tab
from menu.menu_category import category_tab

def menu_screen(app):
    for widget in app.container.winfo_children():
        widget.destroy()

    frame = tk.Frame(app.container)
    frame.pack(fill="both", expand=True)

    tk.Button(frame, text="⬅",
              font=("Arial", 14),
              command=lambda: app.show_screen("main_menu")).pack(anchor="w", padx=10, pady=10)
    
    notebook = ttk.Notebook(frame)
    notebook.pack(fill="both", expand=True)

    # --- Menu Tab
    menu_tab(notebook)

    # --- Menu Category Tab
    category_tab(notebook)
