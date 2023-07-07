
-- Show The total amount spent and the number of orders placed by each customer (if order amount is nonzero)
SELECT customer.Customer_ID, customer.Customer_name, SUM(Orders.Amount) as TotalAmount, count(orders.Order_ID) as NumOrders
FROM customer
INNER JOIN Orders ON customer.Customer_ID = Orders.Customer_ID
GROUP BY customer.Customer_ID, customer.Customer_name
ORDER BY Customer_ID;

-- Show the total number of orders in the month of february 2022
SELECT COUNT(*) as NumOrders, SUM(Amount) as TotalAmount
FROM Orders
WHERE Order_Date >= '2022-02-01' AND Order_Date < '2022-03-01';

-- Increase the price of products with proct ids between 40 and 60 
UPDATE products
SET price = price * 1.1
WHERE product_id >= 40 AND product_id <=60;

-- Show the details of customers with ID >=90 
SELECT * FROM customer
WHERE customer.Customer_ID >= 90;


-- Gives the total revenue availible to be made by each distributor based on the inventory available 
SELECT distributors.distributor_ID, distributors.location, SUM(products.price*inventory.Quantity) AS revenue
FROM distributors
JOIN DISTRIBUTORS_PRODUCTS ON distributors.distributor_ID = DISTRIBUTORS_PRODUCTS.distributor_ID
JOIN products ON DISTRIBUTORS_PRODUCTS.product_ID = products.product_id
JOIN inventory ON products.product_id = inventory.Product_ID
GROUP BY distributors.distributor_ID;



-- Gives the list of all products that are present in the cart with a total amount of >=9
SELECT p.Product_ID,p.product_name
FROM products p
JOIN cart c ON p.product_id = c.Product_ID
WHERE c.Amount >=9
GROUP BY p.product_id
ORDER BY p.product_id;


-- Update the price of product with product id = 3 to 75.99 
UPDATE products
SET price = 75.99
WHERE product_id = 3;


-- Display all the products with more than 3 distributors, in ascending order of their count
SELECT products.product_name, COUNT(DISTINCT DISTRIBUTORS_PRODUCTS.distributor_ID) AS num_distributors
FROM products
INNER JOIN DISTRIBUTORS_PRODUCTS ON products.product_id = DISTRIBUTORS_PRODUCTS.product_ID
GROUP BY products.product_id
HAVING num_distributors > 3
ORDER BY num_distributors;


-- Show the customer details for the order with the highest amount
SELECT customer.Customer_name, customer.Customer_Email, customer.Customer_Contact, customer.Customer_Address, Orders.Amount
FROM customer
INNER JOIN Orders ON customer.Customer_ID = Orders.Customer_ID
WHERE Orders.Amount = (SELECT MAX(Amount) FROM Orders);

-- Query to retreive the top 5 products with the highest revenue  
SELECT p.product_name, SUM(o.Amount * p.price) AS revenue
FROM products p
JOIN inventory i ON p.product_id = i.Product_ID
JOIN Orders o ON o.Customer_ID IN (SELECT Customer_ID FROM customer)
WHERE o.Delivery_Date IS NOT NULL AND i.Quantity >= o.Amount
GROUP BY p.product_id
ORDER BY revenue DESC
LIMIT 5;


