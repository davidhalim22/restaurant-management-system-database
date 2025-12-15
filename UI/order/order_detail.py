from tab_maker import TableFrame

def detail_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Order Detail",
        table_name="Order_Details",
        columns=[
            "order_id",
            "menu_id",
            "quantity",
            "subtotal"
        ],
        pk="order_id",
        add_fields=[
            "order_id", 
            "menu_id", 
            "quantity", 
            "subtotal"
        ],
        optional_fields=[]
    )