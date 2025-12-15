from tab_maker import TableFrame

def table_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Tables",
        table_name="Table_",
        columns=[
            "table_id",
            "capacity",
            "location"
        ],
        pk="table_id",
        add_fields=[
            "capacity", 
            "location", 
        ],
        optional_fields=[]
    )