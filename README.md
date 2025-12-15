Restaurant Database Management System

A simple project that uses MySQL to create and manage a complete restaurant database, including tables for customers, staff, menu, reservations, payments, and orders.
The project also includes sample data and scripts to remove duplicates.

This project is designed to help students learn SQL, database schema design, and basic data management. 


UPDATES: 
- Payment amount in orders now update automatically after each order details entry
- Deleted total amount in order because its not extremely necessary 
- Customer id is now optional when creating order entry as walk-in customers’ data dont need to be recorded (only membership and reservation)
- Deleting entries that other entries depend on no longer crashes the app
- Added a view page with search bar and filter (I didnt merge everything because I think itll be even harder to read)
- Discount table deleted 
- Method_id in orders is no longer NOT NULL (the staff is expected to leave it blank at first then update the info after the customer has paid)