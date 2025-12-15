
ALTER TABLE Orders

DELIMITER $$

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

DELIMITER ;

DELIMITER $$

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

DELIMITER ;

DELIMITER $$

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


