import tkinter as tk
from tkinter import ttk
from database import connect_db

def view_screen(app):
    for widget in app.container.winfo_children():
        widget.destroy()

    frame = tk.Frame(app.container)
    frame.pack(fill="both", expand=True)

    tk.Button(
        frame, text="⬅",
        font=("Arial", 14),
        command=lambda: app.show_screen("main_menu")
    ).pack(anchor="w", padx=10, pady=5)

    tk.Label(
        frame, text="View All Tables",
        font=("Arial", 24, "bold")
    ).pack(pady=(5, 2))

    # ---------- SEARCH BAR ----------
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=(0, 5))

    tk.Label(
        search_frame, text="Search:",
        font=("Arial", 14)
    ).pack(side="left", padx=5)

    search_var = tk.StringVar()
    search_entry = tk.Entry(search_frame, textvariable=search_var, width=40)
    search_entry.pack(side="left", padx=5)

    # ---------- TABLE AREA ----------
    table_container = tk.Frame(frame)
    table_container.pack(fill="both", expand=True)

    tree = ttk.Treeview(table_container, show="headings")
    tree.pack(fill="both", expand=True, side="left")

    v_scroll = ttk.Scrollbar(
        table_container, orient="vertical", command=tree.yview
    )
    v_scroll.pack(side="right", fill="y")

    h_scroll = ttk.Scrollbar(
        frame, orient="horizontal", command=tree.xview
    )
    h_scroll.pack(fill="x")

    tree.configure(
        yscrollcommand=v_scroll.set,
        xscrollcommand=h_scroll.set
    )

    def load_data(keyword=""):
        conn = connect_db()
        cur = conn.cursor()

        sql = """
        SELECT *
        FROM vw_all_data
        WHERE
            source_table LIKE %s OR
            customer_name LIKE %s OR
            staff_name LIKE %s OR
            item_name LIKE %s OR
            CAST(order_id AS CHAR) LIKE %s
        """

        kw = f"%{keyword}%"
        cur.execute(sql, (kw, kw, kw, kw, kw))

        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]

        tree.delete(*tree.get_children())
        tree["columns"] = columns

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=160, anchor="center")

        for row in rows:
            clean_row = ["" if v is None else v for v in row]
            tree.insert("", tk.END, values=clean_row)

        cur.close()
        conn.close()

    # ---------- SEARCH EVENT ----------
    search_entry.bind("<KeyRelease>", lambda e: load_data(search_var.get()))
    
    # ---------------- BUTTONS ----------------
    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=10)

    tk.Button(
        btn_frame,
        text="Refresh",
        font=("Arial", 14),
        command=lambda: load_data("")
    ).pack(side="left", padx=10)

    load_data()
