class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        t=''
        for i in range(0,len(s)):
            if s[i]!='0':
                t+= s[i]
            if t == '':
                return 0
        print(t)
        m=int(t)
        x = sum(int(digit) for digit in t)
        return m*x