1class Solution:
2    def checkOnesSegment(self, s: str) -> bool:
3        if len(s)==1 and s[0]=="1":
4            return True
5        count=0
6        for i in range(1,len(s)):
7            if s[i]=='1' and s[i-1]=='0':
8                count+=1
9            if count>=1:
10                return False
11        return True