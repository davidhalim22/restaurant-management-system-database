USE restaurant_db;

SET SQL_SAFE_UPDATES = 0;



DELETE t1
FROM Table_ t1
JOIN Table_ t2
ON  t1.capacity = t2.capacity
AND t1.location = t2.location
AND t1.table_id > t2.table_id;


DELETE sr1
FROM Staff_Role sr1
JOIN Staff_Role sr2
ON  sr1.role_name = sr2.role_name
AND sr1.role_description = sr2.role_description
AND sr1.staff_role_id > sr2.staff_role_id;


DELETE s1
FROM Staff s1
JOIN Staff s2
ON  s1.staff_name = s2.staff_name
AND s1.staff_phone = s2.staff_phone
AND s1.staff_address = s2.staff_address
AND s1.staff_shift_time = s2.staff_shift_time
AND s1.staff_role_id = s2.staff_role_id
AND s1.staff_id > s2.staff_id;


DELETE mc1
FROM Menu_Category mc1
JOIN Menu_Category mc2
ON  mc1.category_name = mc2.category_name
AND mc1.category_description = mc2.category_description
AND mc1.category_id > mc2.category_id;


DELETE m1
FROM Menu m1
JOIN Menu m2
ON  m1.item_name = m2.item_name
AND m1.item_price = m2.item_price
AND m1.item_description = m2.item_description
AND m1.category_id = m2.category_id
AND m1.menu_id > m2.menu_id;


DELETE d1
FROM Discount_Rate d1
JOIN Discount_Rate d2
ON  d1.discount_name = d2.discount_name
AND d1.discount_value = d2.discount_value
AND d1.discount_id > d2.discount_id;


DELETE mb1
FROM Membership mb1
JOIN Membership mb2
ON  mb1.membership_type = mb2.membership_type
AND mb1.discount_rate = mb2.discount_rate
AND mb1.status = mb2.status
AND mb1.discount_id = mb2.discount_id
AND mb1.membership_id > mb2.membership_id;


DELETE c1
FROM Customer c1
JOIN Customer c2
ON  c1.customer_name = c2.customer_name
AND c1.customer_phone = c2.customer_phone
AND c1.customer_email = c2.customer_email
AND c1.membership_id = c2.membership_id
AND c1.customer_id > c2.customer_id;


DELETE r1
FROM Reservation r1
JOIN Reservation r2
ON  r1.customer_id = r2.customer_id
AND r1.table_id = r2.table_id
AND r1.reservation_date = r2.reservation_date
AND r1.reservation_time = r2.reservation_time
AND r1.status = r2.status
AND r1.reservation_id > r2.reservation_id;


DELETE pm1
FROM Payment_Method pm1
JOIN Payment_Method pm2
ON  pm1.method_name = pm2.method_name
AND pm1.description = pm2.description
AND pm1.is_active = pm2.is_active
AND pm1.method_id > pm2.method_id;


DELETE o1
FROM Orders o1
JOIN Orders o2
ON  o1.customer_id = o2.customer_id
AND o1.staff_id = o2.staff_id
AND o1.table_id = o2.table_id
AND o1.method_id = o2.method_id
AND o1.reservation_id = o2.reservation_id
AND o1.order_date = o2.order_date
AND o1.total_amount = o2.total_amount
AND o1.payment_date = o2.payment_date
AND o1.payment_amount = o2.payment_amount
AND o1.order_id > o2.order_id;


DELETE od1
FROM Order_Details od1
JOIN Order_Details od2
ON  od1.order_id = od2.order_id
AND od1.menu_id = od2.menu_id
AND od1.quantity = od2.quantity
AND od1.subtotal = od2.subtotal
AND (od1.order_id > od2.order_id OR od1.menu_id > od2.menu_id);



SET SQL_SAFE_UPDATES = 1;