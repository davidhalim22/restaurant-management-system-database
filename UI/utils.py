import tkinter as tk
from tkinter import messagebox
from database import connect_db

# GENERIC FETCH & REFRESH FUNCTION
def refresh_table(tree, query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    tree.delete(*tree.get_children())  # Clear table
    for row in rows:
        tree.insert("", tk.END, values=row)

    cursor.close()
    conn.close()

# INSERT FORM POPUP WINDOW
def open_insert_window(title, fields, insert_sql, refresh_callback):
    win = tk.Toplevel()
    win.title(f"Add New {title}")

    entries = {}

    for i, field in enumerate(fields):
        tk.Label(win, text=field + ":").grid(row=i, column=0, padx=5, pady=5, sticky="w")
        entry = tk.Entry(win, width=30)
        entry.grid(row=i, column=1)
        entries[field] = entry

    def submit():
        values = [entries[f].get() for f in fields]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(insert_sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", f"{title} Added.")
        win.destroy()
        refresh_callback()

    tk.Button(win, text="Submit", command=submit).grid(row=len(fields), column=1, pady=10)