# Write your MySQL query statement below
(
    select u.name as results
    from Users u
    join MovieRating m on u.user_id=m.user_id
    group by u.user_id
    order by count(m.rating) desc,u.name asc
    limit 1
)
union all
(
    select mo.title as results
    from Movies mo
    join MovieRating mr on mo.movie_id =mr.movie_id
    where mr.created_at like '2020-02%'
    group by mo.movie_id
    order by avg(mr.rating) desc,mo.title asc
    limit 1
);