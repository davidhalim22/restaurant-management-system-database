from tab_maker import TableFrame

def customer_tab(notebook):
    TableFrame(
    notebook,
    tab_name="Customer",
    table_name="Customer",
    columns=["customer_id","membership_id","customer_name","customer_phone","customer_email"],
    pk="customer_id",
    add_fields=["membership_id","customer_name","customer_phone","customer_email"],
    optional_fields=["membership_id"]   # left blank => stored as NULL
)