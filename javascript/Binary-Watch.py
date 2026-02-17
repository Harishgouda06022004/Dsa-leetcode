1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        if turnedOn>8:
4            return []
5        ans=[]
6        for hour in range(12):
7            for minute in range(60):
8                if hour.bit_count()+ minute.bit_count()==turnedOn:
9                    ans.append(f"{hour}:{minute:02d}")
10        return ans