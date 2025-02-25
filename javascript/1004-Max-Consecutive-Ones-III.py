class Solution(object):
    def longestOnes(self, nums, k):
        maxx=0
        zero_count=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero_count+=1
            while zero_count>k:
                if nums[l]==0:
                    zero_count-=1
                l+=1
            maxx=max(maxx,(r-l)+1)
        return maxx