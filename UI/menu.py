import tkinter as tk
from tkinter import ttk
from utils import refresh_table, open_insert_window

def create_menu_tab(notebook):
    menu_tab = ttk.Frame(notebook)
    notebook.add(menu_tab, text="Menu")

    menu_tree = ttk.Treeview(menu_tab, columns=("ID","Category","Item","Price","Desc"), show="headings")
    for col in ("ID","Category","Item","Price","Desc"):
        menu_tree.heading(col, text=col)
    menu_tree.pack(fill="both", expand=True)

    def refresh_menu():
        refresh_table(
            menu_tree,
            "SELECT menu_id, category_id, item_name, item_price, item_description FROM Menu"
        )

    def add_menu():
        fields = ["menu_id", "category_id", "item_name", "item_price", "item_description"]
        sql = "INSERT INTO Menu (menu_id, category_id, item_name, item_price, item_description) VALUES (%s,%s,%s,%s,%s)"
        open_insert_window("Menu Item", fields, sql, refresh_menu)

    tk.Button(menu_tab, text="Refresh", command=refresh_menu).pack(pady=5)
    tk.Button(menu_tab, text="Add Menu Item", command=add_menu).pack(pady=5)

    refresh_menu()