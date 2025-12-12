from tab_maker import TableFrame

def discount_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Discount",
        table_name="Discount_Rate",
        columns=[
            "discount_id",
            "discount_name",
            "discount_value"
        ],
        pk="discount_id",
        add_fields=[
            ("discount_name", "Discount Name"),
            ("discount_value", "Discount Value")
        ],
        optional_fields=[]
    )