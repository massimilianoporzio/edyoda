# Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT count(*) FROM salespeople WHERE Sname LIKE 'a%' OR Sname LIKE 'A%';
#Display all the Salesperson whose all orders worth is more than Rs. 2000.
SELECT * FROM salespeople s JOIN orders o ON s.snum = o.snum WHERE o.Amt >= 2000; 
#Count the number of Salesperson belonging to Newyork.
SELECT count(*) FROM salespeople s WHERE s.City = 'Newyork';

#Display the number of Salespeople belonging to London and belonging to Paris. Does it mean OR?
#If so the query is
SELECT count(*) FROM salespeople s WHERE s.City = 'Newyork' OR s.City='Paris';
#The formulation with AND (admitting a salesperson belons to TWO cities)
SELECT count(*) FROM salespeople s WHERE s.City = 'Newyork' AND s.City='Paris';
#Display the number of orders taken by each Salesperson and their date of orders.
SELECT s.sname as salesperson, count(o.onum) as num_of_orders , o.Odate as order_date FROM orders o JOIN salespeople s ON o.snum = s.snum GROUP BY s.snum, o.Odate ;