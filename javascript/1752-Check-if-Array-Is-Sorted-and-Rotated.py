class Solution:
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)
        n=len(nums)
        for i in range(n):
            rotated=nums[i:]+nums[:i]
            if s==rotated:
                return True
        return False
