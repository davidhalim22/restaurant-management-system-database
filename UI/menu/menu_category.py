from tab_maker import TableFrame

def category_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Menu Category",
        table_name="Menu_Category",
        columns=[
            "category_id",
            "category_name",
            "category_description"
        ],
        pk="category_id",
        add_fields=[
            "category_name", 
            "category_description"
        ],
        optional_fields=[]
    )