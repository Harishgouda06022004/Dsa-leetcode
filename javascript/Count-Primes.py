class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        # count=0
        # left=2
        # right=n
        # count=0
        
        # for i in range(left,right):
        #     is_prime=True
        #     for j in range(left,int(i**0.5)+1):
        #         if i%j==0:
        #             is_prime=False
        #             break
        #     if is_prime:
        #         count+=1
        # return count
        is_prime=[True]*n
        is_prime[0]=is_prime[1]=False 
        for i in range(2,int(n**0.5)+1,1):
            if is_prime[i]:
                for j in range(i*i,n,i):
                    is_prime[j]=False
        return sum(is_prime)