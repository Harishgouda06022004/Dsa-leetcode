# Write your MySQL query statement below
-- select round(avg(order_date=customer_pref_delivery_date)*100,2) as immediate_percentage
-- from Delivery
-- where(customer_id,order_date) in (
--     select customer_id,min(order_date)
--     from delivery
--     group by customer_id
-- );
select round(avg(d1.order_date=d1.customer_pref_delivery_date)*100,2) as immediate_percentage
from Delivery d1
left join Delivery d2
on d1.customer_id=d2.customer_id
and d1.order_date>d2.order_date
where d2.customer_id is null