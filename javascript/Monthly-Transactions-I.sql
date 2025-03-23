# Write your MySQL query statement below
select substring(trans_date,1,7) as month,country,
count(state) as trans_count,
sum(state="approved") as approved_count,
sum(amount) as trans_total_amount,
SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
from Transactions
group by month,country;
