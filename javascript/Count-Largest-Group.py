class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digsum(n):
            sum1=0
            while n:
                sum1+=n%10
                n//=10
            return sum1
        dict1={}
        maxi,count=0,0
        for i in range(1,n+1):
            x=digsum(i)
            dict1[x]=dict1.get(x,0)+1
            maxi=max(maxi,dict1[x])
        print(dict1)
        for v in dict1.values():
            if v==maxi:
                count+=1
        return count
