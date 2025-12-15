USE restaurant_db;

CREATE OR REPLACE VIEW vw_all_data AS

-- ================= TABLE_ =================
SELECT
    'Table_' AS source_table,
    table_id, capacity, location,
    NULL, NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL
FROM Table_

UNION ALL

-- ================= STAFF_ROLE =================
SELECT
    'Staff_Role',
    NULL, NULL, NULL,
    NULL, NULL, staff_role_id, role_name,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL
FROM Staff_Role

UNION ALL

-- ================= STAFF =================
SELECT
    'Staff',
    NULL, NULL, NULL,
    staff_id, staff_name, staff_role_id, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL
FROM Staff

UNION ALL

-- ================= MENU_CATEGORY =================
SELECT
    'Menu_Category',
    NULL, NULL, NULL,
    NULL, NULL, NULL, NULL,
    category_id, category_name,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL
FROM Menu_Category

UNION ALL

-- ================= MENU =================
SELECT
    'Menu',
    NULL, NULL, NULL,
    NULL, NULL, NULL, NULL,
    category_id, NULL,
    menu_id, item_name, item_price,
    NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL
FROM Menu

UNION ALL

-- ================= MEMBERSHIP =================
SELECT
    'Membership',
    NULL, NULL, NULL,
    NULL, NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    membership_id, discount_rate, membership_type,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL
FROM Membership

UNION ALL

-- ================= CUSTOMER =================
SELECT
    'Customer',
    NULL, NULL, NULL,
    NULL, NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    membership_id, NULL, NULL,
    customer_id, customer_name,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL
FROM Customer

UNION ALL

-- ================= RESERVATION =================
SELECT
    'Reservation',
    table_id, NULL, NULL,
    NULL, NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    customer_id, NULL,
    reservation_id, reservation_date, reservation_time,
    NULL, NULL, NULL,
    NULL, NULL
FROM Reservation

UNION ALL

-- ================= PAYMENT_METHOD =================
SELECT
    'Payment_Method',
    NULL, NULL, NULL,
    NULL, NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    method_id, method_name
FROM Payment_Method

UNION ALL

-- ================= ORDERS =================
SELECT
    'Orders',
    table_id, NULL, NULL,
    staff_id, NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    customer_id, NULL,
    reservation_id, NULL, NULL,
    order_id, order_date, payment_amount,
    method_id, NULL
FROM Orders

UNION ALL

-- ================= ORDER_DETAILS =================
SELECT
    'Order_Details',
    NULL, NULL, NULL,
    NULL, NULL, NULL, NULL,
    NULL, NULL,
    menu_id, NULL, NULL,
    NULL, NULL, NULL,
    NULL, NULL,
    NULL, NULL, NULL,
    order_id, NULL, NULL,
    NULL, NULL
FROM Order_Details;

SELECT source_table, COUNT(*) 
FROM vw_all_data
GROUP BY source_table;