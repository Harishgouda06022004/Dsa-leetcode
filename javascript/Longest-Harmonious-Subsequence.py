# from itertools import combinations
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # n=len(nums)
        # max_length=0
        # for length in range(1,n+1):
        #     for subseq in combinations(nums,length):
        #         if max(subseq)-min(subseq)==1:
        #             m=len(subseq)
        #             max_length=max(max_length,m)
        # return max_length
        # count=Counter(nums)
        # max_len=0
        # for num in count:
        #     if num+1 in count:
        #         max_len=max(max_len,count[num]+count[num+1])
        # return max_len
        nums.sort()
        left=0
        max_len=0
        for right in range(1,len(nums)):
            while nums[right]-nums[left]>1:
                left+=1
            if nums[right]-nums[left]==1:
                max_len=max(max_len,right-left+1)
        return max_len