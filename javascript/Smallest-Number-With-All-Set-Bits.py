class Solution:
    def smallestNumber(self, n: int) -> int:
        t=list(bin(n)[2:])
        for i in range(len(t)):
            if t[i]=='0':
                t[i]='1'
        return int(''.join(t),2)
