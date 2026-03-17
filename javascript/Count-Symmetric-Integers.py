1class Solution:
2    def countSymmetricIntegers(self, low: int, high: int) -> int:
3        count=0
4        for x in range(low,high+1):
5            str_x=str(x)
6            length=len(str_x)
7            if length%2!=0:
8                continue
9            n=length/2
10            sum1=0
11            sum2=0
12            n=int(n)
13            for i in range(0,n):
14                sum1+=int(str_x[i])
15            for j in range(n,length):
16                sum2+=int(str_x[j])
17            if sum1==sum2:
18                count+=1
19        return count
20