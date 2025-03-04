class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # while n>0:
        #     if n%2==2:
        #         return False
        #     n//=2
        # return True
        return n>0 and (n&(n-1))==0