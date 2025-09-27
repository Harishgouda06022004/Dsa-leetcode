class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        curr_sum=0
        max_sum=nums[0]
        for i in range(n):
            if curr_sum<0:
                curr_sum=0
            curr_sum+=nums[i]
            max_sum=max(max_sum,curr_sum)
        return max_sum