class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        l1=[]
        l2=[]
        for i in range(1,n+1):
            if i%m==0:
                l1.append(i)
            else:
                l2.append(i)
        # print(l1)
        # print(l2)
        return sum(l2)-sum(l1)