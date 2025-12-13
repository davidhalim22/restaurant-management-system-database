import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from database import connect_db
import datetime
import mysql.connector

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
def open_insert_window(title, fields, insert_sql, refresh_callback, dropdowns=None, prefill=None):
    win = tk.Toplevel()
    win.title(f"Add New {title}")

    entries = {}
    dropdown_vals = {}

    for i, field in enumerate(fields):
        if isinstance(field, tuple):
            fname, label = field
        else:
            fname, label = field, field

        tk.Label(win, text=f"{label}:").grid(row=i, column=0, padx=5, pady=5, sticky="w")

        if dropdowns and fname in dropdowns:
            q = dropdowns[fname][0]
            display_index = dropdowns[fname][1]
            conn = connect_db()
            cur = conn.cursor()
            cur.execute(q)
            opts = cur.fetchall()
            cur.close()
            conn.close()
            # store mapping value->id
            var = tk.StringVar(win)
            choices = []
            mapping = {}
            for opt in opts:
                # show display text
                display = str(opt[display_index])
                choices.append(display)
                mapping[display] = opt[0]  # assume id is col 0
            if not choices:
                choices = [""]
            var.set(choices[0])
            dropdown_vals[fname] = mapping
            dd = tk.OptionMenu(win, var, *choices)
            dd.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            entries[fname] = var
        else:
            ent = tk.Entry(win, width=40)
            ent.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            if prefill and fname in prefill:
                ent.insert(0, str(prefill[fname]))
            entries[fname] = ent


    def submit():
        values = []
        for f in fields:
            fname = f[0] if isinstance(f, tuple) else f
            widget = entries[fname]
            if fname in (dropdowns or {}):
                # convert selected display back to id value
                display = widget.get()
                val = dropdown_vals[fname].get(display)
                values.append(val)
            else:
                values.append(widget.get() if widget.get() != "" else None)
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute(insert_sql, values)
            conn.commit()
            cur.close()
            conn.close()
            messagebox.showinfo("Success", f"{title} added.")
            win.destroy()
            refresh_callback()
        except Exception as e:
            messagebox.showerror("Error", f"Insert failed:\n{e}")


    tk.Button(win, text="Submit", command=submit).grid(row=len(fields), column=1, pady=10)
    
    
def update_window(title, fields, update_sql, id_field, get_selected_ids, refresh_callback, dropdowns=None):
    ids = get_selected_ids()
    if not ids:
        messagebox.showwarning("No selection", "Please select at least one row to update.")
        return

    win = tk.Toplevel()
    plural = " (multiple rows will be updated)" if len(ids) > 1 else ""
    win.title(f"Update {title}{plural}")

    entries = {}
    dropdown_vals = {}

    for i, (fname, label) in enumerate(fields):
        tk.Label(win, text=f"{label}:").grid(row=i, column=0, padx=5, pady=5, sticky="w")
        if dropdowns and fname in dropdowns:
            q = dropdowns[fname][0]
            display_index = dropdowns[fname][1]
            conn = connect_db()
            cur = conn.cursor()
            cur.execute(q)
            opts = cur.fetchall()
            cur.close()
            conn.close()
            var = tk.StringVar(win)
            choices = []
            mapping = {}
            for opt in opts:
                display = str(opt[display_index])
                choices.append(display)
                mapping[display] = opt[0]
            if not choices:
                choices = [""]
            var.set(choices[0])
            dropdown_vals[fname] = mapping
            dd = tk.OptionMenu(win, var, *choices)
            dd.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            entries[fname] = var
        else:
            ent = tk.Entry(win, width=40)
            ent.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            entries[fname] = ent

    def submit():
        # Build update parameters: values... , id (for each selected id run the update)
        try:
            conn = connect_db()
            cur = conn.cursor()
            for rid in ids:
                params = []
                for (fname, _) in fields:
                    widget = entries[fname]
                    if fname in (dropdowns or {}):
                        display = widget.get()
                        params.append(dropdown_vals[fname].get(display))
                    else:
                        val = widget.get()
                        params.append(val if val != "" else None)
                params.append(rid)
                cur.execute(update_sql, params)
            conn.commit()
            cur.close()
            conn.close()
            messagebox.showinfo("Success", f"{len(ids)} row(s) updated.")
            win.destroy()
            refresh_callback()
        except Exception as e:
            messagebox.showerror("Error", f"Update failed:\n{e}")

    tk.Button(win, text="Submit", command=submit).grid(row=len(fields), column=1, pady=10, sticky="e")



def delete_rows(tree, table_name, pk_fields, refresh_callback):
    sel = tree.selection()
    if not sel:
        messagebox.showwarning("No selection", "Please select at least one row to delete.")
        return

    if not messagebox.askyesno("Confirm Delete", f"Delete {len(sel)} selected row(s)?"):
        return

    conn = connect_db()
    cur = conn.cursor()

    try:
        for item in sel:
            vals = tree.item(item, "values")
            where_clause = " AND ".join([f"{f} = %s" for f in pk_fields])
            sql = f"DELETE FROM {table_name} WHERE {where_clause}"
            params = tuple(vals[i] for i in range(len(pk_fields)))
            cur.execute(sql, params)

        conn.commit()

        messagebox.showinfo("Deleted", f"{len(sel)} row(s) deleted.")
        refresh_callback()

    except mysql.connector.Error as e:
        conn.rollback()

        if e.errno == 1451:
            messagebox.showerror(
                "Delete blocked",
                "This record is referenced by another table.\n"
                "Delete related records first."
            )
        else:
            messagebox.showerror("Database Error", str(e))

    finally:
        cur.close()
        conn.close()
        

def orders_view_tab(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Orders")

    # ================= FILTER BAR =================
    filter_frame = tk.Frame(frame)
    filter_frame.pack(fill="x", padx=10, pady=5)

    tk.Label(filter_frame, text="Min Payment:").pack(side="left")
    min_entry = tk.Entry(filter_frame, width=10)
    min_entry.pack(side="left", padx=5)

    tk.Label(filter_frame, text="Max Payment:").pack(side="left")
    max_entry = tk.Entry(filter_frame, width=10)
    max_entry.pack(side="left", padx=5)

    # ================= TABLE =================
    columns = (
        "order_id",
        "customer_id",
        "staff_id",
        "table_id",
        "payment_amount",
        "order_date"
    )

    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    tree.pack(fill="both", expand=True, padx=10, pady=5)

    # ================= DATA LOADER =================
    def load_orders(min_val=None, max_val=None):
        conn = connect_db()
        cur = conn.cursor()

        if min_val is not None and max_val is not None:
            sql = """
                SELECT order_id, customer_id, staff_id, table_id,
                       payment_amount, order_date
                FROM Orders
                WHERE payment_amount BETWEEN %s AND %s
            """
            cur.execute(sql, (min_val, max_val))
        else:
            sql = """
                SELECT order_id, customer_id, staff_id, table_id,
                       payment_amount, order_date
                FROM Orders
            """
            cur.execute(sql)

        rows = cur.fetchall()
        tree.delete(*tree.get_children())
        for r in rows:
            tree.insert("", tk.END, values=r)

        cur.close()
        conn.close()

    # ================= BUTTON ACTIONS =================
    def apply_filter():
        try:
            min_val = float(min_entry.get())
            max_val = float(max_entry.get())
            load_orders(min_val, max_val)
        except ValueError:
            messagebox.showwarning(
                "Invalid input",
                "Please enter valid numbers for payment amount."
            )

    def clear_filter():
        min_entry.delete(0, tk.END)
        max_entry.delete(0, tk.END)
        load_orders()

    tk.Button(filter_frame, text="Apply Filter", command=apply_filter).pack(side="left", padx=10)
    tk.Button(filter_frame, text="Clear", command=clear_filter).pack(side="left")

    # Initial load
    load_orders()
