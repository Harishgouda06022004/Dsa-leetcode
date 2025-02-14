class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        print(a)
        b=int(b,2)
        print(b)
        c=a+b
        c=bin(c)[2:]
        return c
        