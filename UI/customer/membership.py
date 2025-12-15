from tab_maker import TableFrame

def membership_tab(notebook):
    TableFrame(
        notebook,
        tab_name="Membership",
        table_name="Membership",
        columns=[
            "membership_id",
            "discount_rate",
            "membership_type",
            "status"
        ],
        pk="membership_id",
        add_fields=[        # fields for popup when adding
            "discount_rate",
            "membership_type",
            "status"
        ],
        optional_fields=[]   # leaving this blank becomes NULL in DB
    )