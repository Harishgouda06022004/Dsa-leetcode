1# Write your MySQL query statement below
2select w1.id 
3from Weather w1
4join Weather w2
5on datediff(w1.recordDate,w2.recordDate)=1
6where w1.temperature>w2.temperature