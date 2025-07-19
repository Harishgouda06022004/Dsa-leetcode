class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m=str(n)
        res=0
        product=1
        summ=0
        for i in range(len(m)):
           product*=int(m[i])
           summ+=int(m[i])
        res=product-summ
        print(product)
        print(summ)
        return res