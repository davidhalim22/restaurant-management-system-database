USE restaurant_db;

-- -------------------------------------------------
-- Clean up old triggers (safe to re-run)
-- -------------------------------------------------
DROP TRIGGER IF EXISTS trg_order_details_bi;
DROP TRIGGER IF EXISTS trg_order_details_bu;
DROP TRIGGER IF EXISTS trg_order_details_ai;
DROP TRIGGER IF EXISTS trg_order_details_au;
DROP TRIGGER IF EXISTS trg_order_details_ad;

DELIMITER $$

-- -------------------------------------------------
-- BEFORE INSERT: calculate subtotal
-- -------------------------------------------------
CREATE TRIGGER trg_order_details_bi
BEFORE INSERT ON Order_Details
FOR EACH ROW
BEGIN
    DECLARE price DECIMAL(10,2);

    SELECT item_price
    INTO price
    FROM Menu
    WHERE menu_id = NEW.menu_id;

    SET NEW.subtotal = price * NEW.quantity;
END$$

-- -------------------------------------------------
-- BEFORE UPDATE: recalculate subtotal
-- -------------------------------------------------
CREATE TRIGGER trg_order_details_bu
BEFORE UPDATE ON Order_Details
FOR EACH ROW
BEGIN
    DECLARE price DECIMAL(10,2);

    SELECT item_price
    INTO price
    FROM Menu
    WHERE menu_id = NEW.menu_id;

    SET NEW.subtotal = price * NEW.quantity;
END$$

-- -------------------------------------------------
-- AFTER INSERT: update order total
-- -------------------------------------------------
CREATE TRIGGER trg_order_details_ai
AFTER INSERT ON Order_Details
FOR EACH ROW
BEGIN
    UPDATE Orders
    SET payment_amount = (
        SELECT IFNULL(SUM(subtotal), 0)
        FROM Order_Details
        WHERE order_id = NEW.order_id
    )
    WHERE order_id = NEW.order_id;
END$$

-- -------------------------------------------------
-- AFTER UPDATE: update order total
-- -------------------------------------------------
CREATE TRIGGER trg_order_details_au
AFTER UPDATE ON Order_Details
FOR EACH ROW
BEGIN
    UPDATE Orders
    SET payment_amount = (
        SELECT IFNULL(SUM(subtotal), 0)
        FROM Order_Details
        WHERE order_id = NEW.order_id
    )
    WHERE order_id = NEW.order_id;
END$$

-- -------------------------------------------------
-- AFTER DELETE: update order total
-- -------------------------------------------------
CREATE TRIGGER trg_order_details_ad
AFTER DELETE ON Order_Details
FOR EACH ROW
BEGIN
    UPDATE Orders
    SET payment_amount = (
        SELECT IFNULL(SUM(subtotal), 0)
        FROM Order_Details
        WHERE order_id = OLD.order_id
    )
    WHERE order_id = OLD.order_id;
END$$

DELIMITER ;
