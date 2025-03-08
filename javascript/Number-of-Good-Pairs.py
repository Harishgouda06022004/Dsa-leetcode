from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # dict1={}
        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        # return count
        count=0
        dict1=Counter(nums)
        print(dict1)
        for val in dict1.values():
            count+=val*(val-1)//2
        return count