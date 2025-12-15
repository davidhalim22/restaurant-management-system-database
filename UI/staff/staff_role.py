from tab_maker import TableFrame

def role_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Staff Role",
        table_name="Staff_Role",
        columns=[
            "staff_role_id",
            "role_name",
            "role_description"
        ],
        pk="staff_role_id",
        add_fields=[
            "role_name", 
            "role_description",
        ],
        optional_fields=[]
    )