1class Solution:
2    def check(self, nums: List[int]) -> bool:
3        s=sorted(nums)
4        for i in range(len(nums)):
5            rotated=nums[i:]+nums[:i]
6            if s==rotated:
7                return True
8        return False