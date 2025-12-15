import tkinter as tk
from tkinter import ttk
from staff.staff import staff_tab
from staff.staff_role import role_tab


def staff_screen(app):
    for widget in app.container.winfo_children():
        widget.destroy()

    frame = tk.Frame(app.container)
    frame.pack(fill="both", expand=True)

    tk.Button(frame, text="⬅",
              font=("Arial", 14),
              command=lambda: app.show_screen("main_menu")).pack(anchor="w", padx=10, pady=10)
    
    notebook = ttk.Notebook(frame)
    notebook.pack(fill="both", expand=True)

    # --- Staff Tab
    staff_tab(notebook)

    # --- Staff Role Tab
    role_tab(notebook)