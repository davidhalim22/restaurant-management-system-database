from tab_maker import TableFrame

def menu_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Menu",
        table_name="Menu",
        columns=[
            "menu_id",
            "category_id",
            "item_name",
            "item_price",
            "item_description"
        ],
        pk="menu_id",
        add_fields=[
            "category_id", 
            "item_name", 
            "item_price",
            "item_description", 
        ],
        optional_fields=[]
    )