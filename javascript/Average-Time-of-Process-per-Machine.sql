1# Write your MySQL query statement below
2select a.machine_id,round(avg(b.timestamp-a.timestamp),3) as processing_time
3from activity a
4join activity b
5on a.machine_id=b.machine_id
6and a.process_id=b.process_id
7and a.activity_type ='start'
8and b.activity_type ='end'
9group by b.machine_id