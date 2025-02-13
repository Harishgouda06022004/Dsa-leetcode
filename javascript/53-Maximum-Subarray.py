class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n=len(nums)
        # max_sum=float('-inf')
        # for i in range(0,n):
        #     current_sum=0
        #     for j in range(i,n):
        #         current_sum+=nums[j]
        #         max_sum=max(current_sum,max_sum)
        # return max_sum
        max_sum=nums[0]
        curr_sum=0
        for n in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=n
            max_sum=max(max_sum,curr_sum)
        return max_sum