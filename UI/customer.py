import tkinter as tk
from tkinter import ttk
from utils import refresh_table, open_insert_window

def create_customer_tab(notebook):
    customer_tab = ttk.Frame(notebook)
    notebook.add(customer_tab, text="Customers")

    customer_tree = ttk.Treeview(customer_tab, columns=("ID","Membership","Name","Phone","Email"), show="headings")
    for col in ("ID","Membership","Name","Phone","Email"):
        customer_tree.heading(col, text=col)
    customer_tree.pack(fill="both", expand=True)

    def refresh_customer():
        refresh_table(
            customer_tree,
            "SELECT customer_id, membership_id, customer_name, customer_phone, customer_email FROM Customer"
        )

    def add_customer():
        fields = ["customer_id", "membership_id", "customer_name", "customer_phone", "customer_email"]
        sql = "INSERT INTO Customer (customer_id, membership_id, customer_name, customer_phone, customer_email) VALUES (%s,%s,%s,%s,%s)"
        open_insert_window("Customer", fields, sql, refresh_customer)

    tk.Button(customer_tab, text="Refresh", command=refresh_customer).pack(pady=5)
    tk.Button(customer_tab, text="Add Customer", command=add_customer).pack(pady=5)

    refresh_customer()