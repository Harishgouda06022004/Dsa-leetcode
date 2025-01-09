class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        low=1
        high=num
        while low<=high:
            mid=(low+high)//2
            if mid * mid <num:
                low = mid + 1.
            elif mid * mid >num:
                high=mid-1
            elif mid*mid==num:
                return True
        return False