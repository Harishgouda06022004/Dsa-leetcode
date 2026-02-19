1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        res=0
4        prev=0
5        strk=1
6        for i in range(1,len(s)):
7            if s[i]==s[i-1]:
8                strk+=1
9            else:
10                prev=strk
11                strk=1
12            if strk<=prev:
13                res+=1
14        return res