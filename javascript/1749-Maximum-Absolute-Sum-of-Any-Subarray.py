class Solution(object):
    def maxAbsoluteSum(self, nums):
        # curr_sum=0
        # max_sum=float('-inf')
        # n=len(nums)
        # for i in range(n):
        #     curr_sum=0
        #     for j in range(i,n):
        #         curr_sum+=nums[j]
        #         max_sum=max(max_sum,abs(curr_sum))
        # return max_sum
        max_sum=0
        min_sum=0
        curr_max=0
        curr_min=0
        for num in nums:
            curr_max=max(num,curr_max+num)
            curr_min=min(num,curr_min+num)
            max_sum=max(max_sum,curr_max)
            min_sum=min(min_sum,curr_min)
        return max(abs(max_sum),abs(min_sum))