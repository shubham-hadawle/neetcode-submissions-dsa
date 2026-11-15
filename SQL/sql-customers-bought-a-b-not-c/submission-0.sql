-- Write your query below
SELECT customers.customer_id, customer_name
FROM customers -- LEFT JOIN orders on customers.customer_id = orders.customer_id (This JOIN cannot be used)
WHERE customers.customer_id IN (SELECT customer_id FROM orders WHERE product_name = 'A')
    AND customers.customer_id IN (SELECT customer_id FROM orders WHERE product_name = 'B')
    AND customers.customer_id NOT IN (SELECT customer_id FROM orders WHERE product_name = 'C')
ORDER BY customer_name;