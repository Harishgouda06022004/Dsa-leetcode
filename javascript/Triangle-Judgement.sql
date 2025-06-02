# Write your MySQL query statement below
-- select x,y,z,triangle
-- from Triangle
-- where x+y>z
-- select *,if(x+y>z and y+z>x and z+x>y,\Yes\,\No\) as triangle from Triangle
select *,if(x+y>z and y+z>x and z+x>y,\Yes\,\No\) as triangle from Triangle