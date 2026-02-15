1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        c=int(a,2)
4        d=int(b,2)
5        e=c+d
6        return bin(e)[2:]