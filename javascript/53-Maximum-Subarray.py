class Solution(object):
    def maxSubArray(self, nums):
        curr_sum=0
        max_sum=float(\-inf\) #kadanes algorithm
        n=len(nums)
        for i in range(n):
            curr_sum+=nums[i]
            max_sum=max(curr_sum,max_sum)
            if curr_sum<0:
                curr_sum=0
        return max_sum