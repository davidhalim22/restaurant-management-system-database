from tab_maker import TableFrame

def order_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Order",
        table_name="Orders",
        columns=[
            "order_id",
            "customer_id",
            "staff_id",
            "table_id",
            "method_id",
            "reservation_id",
            "order_date",
            "total_amount",
            "payment_date",
            "payment_amount"
        ],
        pk="order_id",
        add_fields=[
            ("customer_id", "Customer ID"),
            ("staff_id", "Staff ID"),
            ("table_id", "Table ID"),
            ("method_id", "Payment Method ID"),
            ("reservation_id", "Reservation ID"),
            ("order_date", "Order Date"),
            ("total_amount", "Total Amount"),
            ("payment_date", "Payment Date"),
            ("payment_amount", "Payment Amount")
        ],
        optional_fields=[]
    )