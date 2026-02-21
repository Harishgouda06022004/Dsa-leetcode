1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        count=0
4        for i in range(left,right+1):
5            setBits=bin(i).count('1')
6            if self.isPrime(setBits):
7                count+=1
8        return count
9
10
11    def isPrime(self,n: int) -> bool:
12        if n<=1:
13            return False
14        for i in range(2,int(n**0.5)+1):
15            if n%i==0:
16                return False
17        return True
18