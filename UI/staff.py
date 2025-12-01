import tkinter as tk
from tkinter import ttk
from utils import refresh_table, open_insert_window

def create_staff_tab(notebook):
    staff_tab = ttk.Frame(notebook)
    notebook.add(staff_tab, text="Staff")

    staff_tree = ttk.Treeview(staff_tab, columns=("ID","Role","Name","Address","Phone","Shift"), show="headings")
    for col in ("ID","Role","Name","Address","Phone","Shift"):
        staff_tree.heading(col, text=col)
    staff_tree.pack(fill="both", expand=True)

    def refresh_staff():
        refresh_table(
            staff_tree,
            "SELECT staff_id, staff_role_id, staff_name, staff_address, staff_phone, staff_shift_time FROM Staff"
        )

    def add_staff():
        fields = ["staff_id", "staff_role_id", "staff_name", "staff_address", "staff_phone", "staff_shift_time"]
        sql = "INSERT INTO Staff (staff_id, staff_role_id, staff_name, staff_address, staff_phone, staff_shift_time) VALUES (%s,%s,%s,%s,%s,%s)"
        open_insert_window("Staff", fields, sql, refresh_staff)

    tk.Button(staff_tab, text="Refresh", command=refresh_staff).pack(pady=5)
    tk.Button(staff_tab, text="Add Staff", command=add_staff).pack(pady=5)

    refresh_staff()