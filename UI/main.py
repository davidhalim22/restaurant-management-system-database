import tkinter as tk
from tkinter import ttk
from customer.customer_screen import customer_screen
from menu.menu_screen import menu_screen
from order.order_screen import order_screen
from staff.staff_screen import staff_screen
from view import view_screen; 


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant Management System")
        self.geometry("1600x900")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.screens = {
            "main_menu": lambda app: self.main_menu()
        }

 
        self.screens["customer"] = customer_screen
        self.screens["menu"] = menu_screen
        self.screens["order"] = order_screen
        self.screens["staff"] = staff_screen
        self.screens["view"] = view_screen

        self.show_screen("main_menu")

    def show_screen(self, name):
        for w in self.container.winfo_children():
            w.destroy()

        screen_callable = self.screens.get(name)
        if not screen_callable:
            raise ValueError(f"Screen '{name}' not found")
        screen_callable(self)

    def main_menu(self):
        frame = tk.Frame(self.container)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Restaurant Management System",
                 font=("Arial", 32, "bold")).pack(pady=40)

        tk.Button(frame, text="Customer Management", font=("Arial", 18), width=30,
                  command=lambda: self.show_screen("customer")).pack(pady=12)

        tk.Button(frame, text="Order Management", font=("Arial", 18), width=30,
                  command=lambda: self.show_screen("order")).pack(pady=12)

        tk.Button(frame, text="Menu Management", font=("Arial", 18), width=30,
                  command=lambda: self.show_screen("menu")).pack(pady=12)

        tk.Button(frame, text="Staff Management", font=("Arial", 18), width=30,
                  command=lambda: self.show_screen("staff")).pack(pady=12)

        tk.Button(frame, text="View", font=("Arial", 18), width=30,
                  command=lambda: self.show_screen("view")).pack(pady=12)

        tk.Button(frame, text="Exit", font=("Arial", 18), width=30,
                  command=self.destroy).pack(pady=12)


if __name__ == "__main__":
    app = App()
    app.mainloop()