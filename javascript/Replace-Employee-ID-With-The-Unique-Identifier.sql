# Write your MySQL query statement below
-- SELECT euni.unique_id,e.name
-- FROM Employees e
-- LEFT JOIN EmployeeUNI euni
-- ON e.id=euni.id;
select euni.unique_id,e.name
from Employees e
left join EmployeeUNI euni
on e.id=euni.id