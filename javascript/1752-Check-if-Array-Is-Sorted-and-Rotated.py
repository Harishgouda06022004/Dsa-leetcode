class Solution:
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)
        for i in range(len(nums)):
            rotated=nums[i:]+nums[:i]
            if s==rotated:
                return True
        return False