1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        first_upper={}
4        last_lower={}
5        for i,ch in enumerate(word):
6            if ch.islower():
7                last_lower[ch]=i
8            else:
9                c=ch.lower()
10                if c not in first_upper:
11                    first_upper[c]=i
12        ans=0
13        for c in last_lower:
14            if c in first_upper and last_lower[c]<first_upper[c]:
15                ans+=1
16        return ans