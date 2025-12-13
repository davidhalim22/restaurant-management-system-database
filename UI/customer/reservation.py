from tab_maker import TableFrame

def reservation_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Reservation",
        table_name="Reservation",
        columns=[
            "reservation_id",
            "customer_id",
            "table_id",
            "reservation_date",
            "reservation_time",
            "status"
        ],
        pk="reservation_id",
        add_fields=[
            "customer_id", 
            "table_id", 
            "reservation_date", 
            "reservation_time", 
            "status", 
        ],
        optional_fields=[]
    )