import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db


class TableFrame(ttk.Frame):
    def __init__(self, notebook, tab_name, table_name, columns, pk, add_fields, optional_fields=None):
        """
        notebook       - ttk.Notebook parent
        tab_name       - name to show on the tab
        table_name     - DB table name
        columns        - list of column names shown in the UI
        pk             - primary key column name
        add_fields     - fields that user types when adding (PK excluded!)
        optional_fields - list of fields allowed to be NULL (blank input -> NULL)
        """
        super().__init__(notebook)
        notebook.add(self, text=tab_name)

        self.table_name = table_name
        self.columns = columns
        self.pk = pk
        self.add_fields = add_fields
        self.optional_fields = optional_fields if optional_fields else []

        # ---- TreeView ----
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")
        for c in self.columns:
            self.tree.heading(c, text=c, anchor="center")
            self.tree.column(c, width=150, anchor="center")
        self.tree.pack(fill="both", expand=True)

        # Buttons
        btn = tk.Frame(self)
        btn.pack(fill="x", pady=6)
        tk.Button(btn, text="Refresh", command=self.refresh).pack(side="left", padx=6)
        tk.Button(btn, text="Add", command=self.add_row_popup).pack(side="left", padx=6)
        tk.Button(btn, text="Update", command=self.update_row_popup).pack(side="left", padx=6)
        tk.Button(btn, text="Delete", command=self.delete_selected).pack(side="left", padx=6)

        self.tree.bind("<Double-1>", self.inline_edit)

        self.refresh()

    def refresh(self):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"SELECT {','.join(self.columns)} FROM {self.table_name} ORDER BY {self.pk}")
        rows = cur.fetchall()
        self.tree.delete(*self.tree.get_children())
        for r in rows:
            self.tree.insert("", tk.END, values=r)
        cur.close(); conn.close()

    def add_row_popup(self):
        win = tk.Toplevel(self)
        win.transient(self)
        win.grab_set()
        win.focus_force()

        win.title(f"Add to {self.table_name}")
        entries = {}

        for i, f in enumerate(self.add_fields):
            tk.Label(win, text=f + ":").grid(row=i, column=0, padx=6, pady=4, sticky="w")
            e = tk.Entry(win, width=35)
            e.grid(row=i, column=1)
            entries[f] = e

        def submit():
            values = []
            for field in self.add_fields:
                v = entries[field].get().strip()
                if field in self.optional_fields and v == "":
                    values.append(None)
                else:
                    values.append(v)

            conn = connect_db(); cur = conn.cursor()
            sql = f"INSERT INTO {self.table_name} ({','.join(self.add_fields)}) VALUES ({','.join(['%s']*len(values))})"
            try:
                cur.execute(sql, values)
                conn.commit()
                win.destroy()
                self.refresh()
                messagebox.showinfo("Success", "Row added.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            cur.close(); conn.close()

        tk.Button(win, text="Submit", command=submit).grid(row=len(self.add_fields), column=1, pady=10)


    def update_row_popup(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Select rows first.")
            return

        win = tk.Toplevel(self)
        win.transient(self)
        win.grab_set()
        win.focus_force()

        win.title(f"Update {self.table_name}")
        entries = {}

        fields_to_edit = [c for c in self.columns if c != self.pk]
        for i, f in enumerate(fields_to_edit):
            tk.Label(win, text=f + ":").grid(row=i, column=0, padx=6, pady=4, sticky="w")
            e = tk.Entry(win, width=35)
            e.grid(row=i, column=1)
            entries[f] = e

        def submit():
            conn = connect_db(); cur = conn.cursor()
            for item in selected:
                row = self.tree.item(item, "values")
                pk_value = row[self.columns.index(self.pk)]

                values = []
                for f in fields_to_edit:
                    v = entries[f].get().strip()
                    if f in self.optional_fields and v == "":
                        values.append(None)
                    else:
                        values.append(v)

                set_sql = ", ".join([f"{f}=%s" for f in fields_to_edit])
                cur.execute(f"UPDATE {self.table_name} SET {set_sql} WHERE {self.pk}=%s", (*values, pk_value))

            conn.commit()
            cur.close(); conn.close()
            win.destroy()
            self.refresh()
            messagebox.showinfo("Updated", f"{len(selected)} row(s) updated.")

        tk.Button(win, text="Submit", command=submit).grid(row=len(fields_to_edit), column=1, pady=10)

    # ---------- DELETE ----------
    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Select row(s) to delete.")
            return
        if not messagebox.askyesno("Confirm", "Delete selected rows?"):
            return

        conn = connect_db(); cur = conn.cursor()
        for item in selected:
            pk_value = self.tree.item(item, "values")[self.columns.index(self.pk)]
            cur.execute(f"DELETE FROM {self.table_name} WHERE {self.pk}=%s", (pk_value,))
        conn.commit()
        cur.close(); conn.close()
        self.refresh()

    # ---------- INLINE EDIT ----------
    def inline_edit(self, event):
        rowid = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)
        if not rowid or column == "#1":
            return

        col_index = int(column.replace("#", "")) - 1
        x, y, w, h = self.tree.bbox(rowid, column)
        abs_x = self.tree.winfo_rootx() + x
        abs_y = self.tree.winfo_rooty() + y

        current = list(self.tree.item(rowid, "values"))
        current_value = current[col_index]

        win = tk.Toplevel(self)
        win.overrideredirect(True)
        win.geometry(f"{w}x{h}+{abs_x}+{abs_y}")
        entry = tk.Entry(win)
        entry.insert(0, "" if current_value is None else str(current_value))
        entry.pack(fill="both", expand=True)
        entry.focus()

        def commit(event=None):
            new = entry.get()
            win.destroy()
            if new == ("" if current_value is None else str(current_value)):
                return

            col_name = self.columns[col_index]
            if col_name in self.optional_fields and new.strip() == "":
                db_value = None
            else:
                db_value = new

            current[col_index] = db_value
            self.tree.item(rowid, values=current)

            pk_value = current[self.columns.index(self.pk)]
            conn = connect_db(); cur = conn.cursor()
            sql = f"UPDATE {self.table_name} SET {col_name}=%s WHERE {self.pk}=%s"
            cur.execute(sql, (db_value, pk_value))
            conn.commit()
            cur.close(); conn.close()

        entry.bind("<Return>", commit)
        entry.bind("<Escape>", lambda e: win.destroy())