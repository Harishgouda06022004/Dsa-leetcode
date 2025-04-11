class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for x in range(low,high+1):
            str_x=str(x)
            length=len(str_x)
            if length%2!=0:
                continue
            n=length/2
            sum1=0
            sum2=0
            n=int(n)
            for i in range(0,n):
                sum1+=int(str_x[i])
            for j in range(n,length):
                sum2+=int(str_x[j])
            if sum1==sum2:
                count+=1
        return count