class Solution(object):
    def climbStairs(self, n):
        if n<=3:
            return n
        fib1=1
        fib2=2
        for i in range(3,n+1):
            fib1,fib2=fib2,fib1+fib2
            print(fib1)
            print(fib2)
        return fib2