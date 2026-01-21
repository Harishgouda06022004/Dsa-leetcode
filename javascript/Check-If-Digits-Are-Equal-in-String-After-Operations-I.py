1class Solution:
2    def hasSameDigits(self, s: str) -> bool:
3        while len(s)>2:
4            new_s=""
5            for i in range(len(s)-1):
6                new_s+=str((int(s[i])+int(s[i+1]))%10)
7            s=new_s
8        print(s)
9        if s[0]==s[1]:
10            return True
11        else:
12            return False