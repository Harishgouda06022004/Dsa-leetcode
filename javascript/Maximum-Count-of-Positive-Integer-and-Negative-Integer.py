class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count=0
        count2=0
        for n in nums:
            if n>0:
                count+=1
            if n<0:
                count2+=1
        return max(count,count2)