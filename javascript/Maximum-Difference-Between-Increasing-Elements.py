class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_nums=-1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]<nums[j]:
                    max_nums=max(max_nums,nums[j]-nums[i]) 
        return max_nums