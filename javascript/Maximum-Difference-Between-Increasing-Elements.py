class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val=nums[0]
        max_nums=-1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i<j and nums[i]<nums[j]:
        #             max_nums=max(max_nums,nums[j]-nums[i]) 
        # return max_nums
        for j in range(1,len(nums)):
            if nums[j]>min_val:
                max_nums=max(max_nums,nums[j]-min_val)
            else:
                min_val=nums[j]
        return max_nums