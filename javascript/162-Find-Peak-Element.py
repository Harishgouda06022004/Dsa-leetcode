class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # n=len(nums)
        # for i in range(0,n):
        return nums.index(max(nums))
