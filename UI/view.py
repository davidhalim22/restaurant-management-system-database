import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db
from utils import orders_view_tab

def view_table_tab(notebook, tab_name, table_name):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=tab_name)

    # --- Search Bar ---
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", padx=10, pady=5)

    tk.Label(search_frame, text="Search:").pack(side="left")

    search_var = tk.StringVar()
    search_entry = tk.Entry(search_frame, textvariable=search_var, width=40)
    search_entry.pack(side="left", padx=5)

    # --- Treeview ---
    tree = ttk.Treeview(frame, show="headings")
    tree.pack(fill="both", expand=True, padx=10, pady=5)

    # --- Load columns dynamically ---
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(f"DESCRIBE {table_name}")
    columns = [col[0] for col in cur.fetchall()]
    cur.close()
    conn.close()

    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=130, anchor="center")

    # --- Refresh Function ---
    def refresh(query=None):
        tree.delete(*tree.get_children())
        conn = connect_db()
        cur = conn.cursor()

        if query:
            cur.execute(query)
        else:
            cur.execute(f"SELECT * FROM {table_name}")

        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)

        cur.close()
        conn.close()

    refresh()

    # --- Search Logic ---
    def search():
        text = search_var.get().strip()
        if not text:
            refresh()
            return

        where_clause = " OR ".join([f"{c} LIKE %s" for c in columns])
        sql = f"SELECT * FROM {table_name} WHERE {where_clause}"
        params = tuple([f"%{text}%"] * len(columns))

        tree.delete(*tree.get_children())
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(sql, params)

        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)

        cur.close()
        conn.close()

    tk.Button(search_frame, text="Search", command=search).pack(side="left", padx=5)
    tk.Button(search_frame, text="Reset", command=refresh).pack(side="left")


def view_screen(app):
    for widget in app.container.winfo_children():
        widget.destroy()

    frame = tk.Frame(app.container)
    frame.pack(fill="both", expand=True)

    tk.Button(frame, text="⬅",
              font=("Arial", 14),
              command=lambda: app.show_screen("main_menu")
    ).pack(anchor="w", padx=10, pady=10)

    notebook = ttk.Notebook(frame)
    notebook.pack(fill="both", expand=True)

    # ---- View Tabs ----
    view_table_tab(notebook, "Customers", "Customer")
    view_table_tab(notebook, "Menu", "Menu")
    view_table_tab(notebook, "Staff", "Staff")
    
    notebook = ttk.Notebook(frame)
    notebook.pack(fill="both", expand=True)

    # 👇 THIS IS WHERE IT RUNS
    orders_view_tab(notebook)

