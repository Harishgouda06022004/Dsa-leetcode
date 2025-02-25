class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count=0
        count=0
        for num in nums:
            if num==1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=0
        return max(max_count,count)
            
        