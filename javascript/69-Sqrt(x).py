class Solution:
    def mySqrt(self, x: int) -> int:
        low=1
        high=x
        while low<=high:
            mid=(low+high)//2
            Mid_squared=mid*mid
            if Mid_squared==x:
                return mid
            elif Mid_squared<x:
                low=mid+1
            else:
                high=mid-1
        return high