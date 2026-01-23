1class Solution:
2    def totalMoney(self, n: int) -> int:
3        total=0
4        week_start=1
5        for i in range(1,n+1):
6            day_of_week=(i-1)%7
7            total+=week_start+day_of_week
8            if day_of_week==6:
9                week_start+=1
10        return total
11            
12