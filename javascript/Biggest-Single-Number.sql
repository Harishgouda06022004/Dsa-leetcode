# Write your MySQL query statement below
-- select max(num) as num
-- from myNumbers
-- where num in(
--     select num
--     from myNumbers
--     group by num
--     having count(num)=1
-- )
select max(num) as num
from MyNumbers
where num in(
    select num
    from MyNumbers
    group by num
    having count(num)=1
)