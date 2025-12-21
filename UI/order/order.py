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
            "payment_date",
            "payment_amount"
        ],
        pk="order_id",
        add_fields=[
            "customer_id", 
            "staff_id", 
            "table_id", 
            "method_id", 
            "reservation_id", 
            "order_date", 
            "payment_date"
        ],
        optional_fields=["customer_id","reservation_id", "payment_date", "payment_amount","method_id"]
    )