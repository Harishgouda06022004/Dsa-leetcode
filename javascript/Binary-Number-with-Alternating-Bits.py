1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        s=bin(n)[2:]
4        for i in range(len(s)-1):
5            if s[i]==s[i+1]:
6                return False
7        return True