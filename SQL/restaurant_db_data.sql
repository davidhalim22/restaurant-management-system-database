USE restaurant_db;

INSERT INTO Table_ (capacity, location) VALUES
(2, 'Window'),
(4, 'Center'),
(6, 'VIP Room');

INSERT INTO Staff_Role (role_name, role_description) VALUES
('Waiter', 'Serves customers'),
('Chef', 'Prepares meals'),
('Cashier', 'Handles billing');

INSERT INTO Staff (staff_role_id, staff_name, staff_address, staff_phone, staff_shift_time) VALUES
(1, 'Alice Lim', 'Jl. Merdeka 10', '081234567890', 'Morning'),
(2, 'Budi Setiawan', 'Jl. Mawar 23', '082345678901', 'Evening'),
(3, 'Cindy Hartono', 'Jl. Anggrek 5', '083456789012', 'Afternoon');

INSERT INTO Menu_Category (category_name, category_description) VALUES
('Drinks', 'Beverages'),
('Main Course', 'Meals'),
('Dessert', 'Sweet dishes');

INSERT INTO Menu (category_id, item_name, item_price, item_description) VALUES
(1, 'Iced Tea', 1.50, 'Cold sweet tea'),
(2, 'Chicken Rice', 5.00, 'Steamed rice with chicken'),
(3, 'Chocolate Cake', 3.50, 'Rich chocolate flavor');

INSERT INTO Discount_Rate (discount_name, discount_value) VALUES
('None', 0.00),
('Silver', 5.00),
('Gold', 10.00);

INSERT INTO Membership (discount_id, membership_type, discount_rate, status) VALUES
(1, 'Regular', 0.00, 'Active'),
(2, 'Silver Member', 5.00, 'Active'),
(3, 'Gold Member', 10.00, 'Inactive');

INSERT INTO Customer (membership_id, customer_name, customer_phone, customer_email) VALUES
(1, 'Daniel Tan', '0811111111', 'daniel@example.com'),
(2, 'Eva Michelle', '0822222222', 'eva@example.com'),
(3, 'Felix Wong', '0833333333', 'felix@example.com');

INSERT INTO Reservation (customer_id, table_id, reservation_date, reservation_time, status) VALUES
(1, 1, '2025-01-10', '18:00:00', 'Confirmed'),
(2, 2, '2025-01-11', '19:00:00', 'Pending'),
(3, 3, '2025-01-12', '20:30:00', 'Completed');

INSERT INTO Payment_Method (method_name, description, is_active) VALUES
('Cash', 'Pay with cash', TRUE),
('Credit Card', 'Visa/Mastercard', TRUE),
('E-Wallet', 'OVO/Gopay/etc', TRUE);

INSERT INTO Orders (
    customer_id, staff_id, table_id, method_id, reservation_id,
    order_date, total_amount, payment_date, payment_amount
) VALUES
(1, 1, 1, 1, 1, '2025-01-10 18:30:00', 6.50, '2025-01-10 19:00:00', 6.50),
(2, 2, 2, 2, 2, '2025-01-11 19:10:00', 8.50, '2025-01-11 19:40:00', 8.50),
(3, 3, 3, 3, 3, '2025-01-12 20:45:00', 3.50, '2025-01-12 21:00:00', 3.50);

INSERT INTO Order_Details (order_id, menu_id, quantity, subtotal) VALUES
(1, 1, 1, 1.50),
(1, 2, 1, 5.00),
(2, 2, 1, 5.00),
(2, 3, 1, 3.50),
(3, 3, 1, 3.50);
