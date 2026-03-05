1class Solution:
2    def minOperations(self, s: str) -> int:
3        change1=0
4        change2=0
5        for i in range(len(s)):
6            if i%2==0:
7                if s[i]!='0':
8                    change1+=1
9                if s[i]!='1':
10                    change2+=1
11            else:
12                if s[i]!='1':
13                    change1+=1
14                if s[i]!='0':
15                    change2+=1
16        return min(change1,change2)
17
18