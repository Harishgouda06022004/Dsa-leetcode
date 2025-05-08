# Write your MySQL query statement below
-- SELECT p.product_name,s.year,s.price
-- FROM Sales s
-- JOIN Product p
-- ON s.product_id=p.product_id
select p.product_name,s.year,s.price
from Sales s
inner join Product p
on p.product_id=s.product_id
