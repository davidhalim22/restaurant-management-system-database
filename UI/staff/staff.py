from tab_maker import TableFrame


def staff_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Staff",
        table_name="Staff",
        columns=[
            "staff_id",
            "staff_role_id",
            "staff_name",
            "staff_phone",
            "staff_address",
            "staff_shift_time"
        ],
        pk="staff_id",
        add_fields=[
            "staff_role_id", 
            "staff_name", 
            "staff_phone",
            "staff_address", 
            "staff_shift_time", 
        ],
        optional_fields=[]
    )
