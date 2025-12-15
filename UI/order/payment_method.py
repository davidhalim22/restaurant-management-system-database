from tab_maker import TableFrame

def payment_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Payment Method",
        table_name="Payment_Method",
        columns=[
            "method_id",
            "method_name",
            "is_active"
        ],
        pk="method_id",
        add_fields=[
            "method_name", 
            "is_active", 
        ],
        optional_fields=[]
    )