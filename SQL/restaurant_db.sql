DROP DATABASE IF EXISTS restaurant_db;
CREATE DATABASE IF NOT EXISTS restaurant_db;
USE restaurant_db;

CREATE TABLE Table_ (
    table_id INT AUTO_INCREMENT PRIMARY KEY,
    capacity INT NOT NULL,
    location VARCHAR(100)
);

CREATE TABLE Staff_Role (
    staff_role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(100) NOT NULL,
    role_description VARCHAR(100)
);

CREATE TABLE Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_role_id INT NOT NULL,
    staff_name VARCHAR(150) NOT NULL,
    staff_address VARCHAR(255),
    staff_phone VARCHAR(30),
    staff_shift_time VARCHAR(100),
    FOREIGN KEY (staff_role_id) REFERENCES Staff_Role(staff_role_id)
);

CREATE TABLE Menu_Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    category_description VARCHAR(300) 
);

CREATE TABLE Menu (
    menu_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    item_name VARCHAR(150) NOT NULL,
    item_price DECIMAL(10,2) NOT NULL,
    item_description VARCHAR(300),
    FOREIGN KEY (category_id) REFERENCES Menu_Category(category_id)
);


CREATE TABLE Membership (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    discount_rate INT NOT NULL,
    membership_type VARCHAR(100),
    status VARCHAR(50)
);

CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    membership_id INT,
    customer_name VARCHAR(150) NOT NULL,
    customer_phone VARCHAR(30),
    customer_email VARCHAR(150),
    FOREIGN KEY (membership_id) REFERENCES Membership(membership_id)
);

CREATE TABLE Reservation (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    table_id INT NOT NULL,
    reservation_date DATE,
    reservation_time TIME,
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (table_id) REFERENCES Table_(table_id)
);

CREATE TABLE Payment_Method (
    method_id INT AUTO_INCREMENT PRIMARY KEY,
    method_name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    staff_id INT NOT NULL,
    table_id INT NOT NULL,
    method_id INT NOT NULL,
    reservation_id INT,
    order_date DATETIME,
    payment_date DATETIME DEFAULT NULL ,
    payment_amount DECIMAL(10,2) DEFAULT NULL, 
    
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id),
    FOREIGN KEY (table_id) REFERENCES Table_(table_id),
    FOREIGN KEY (method_id) REFERENCES Payment_Method(method_id),
    FOREIGN KEY (reservation_id) REFERENCES Reservation(reservation_id)
);

CREATE TABLE Order_Details (
    order_id INT NOT NULL,
    menu_id INT NOT NULL,
    quantity INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, menu_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
);

