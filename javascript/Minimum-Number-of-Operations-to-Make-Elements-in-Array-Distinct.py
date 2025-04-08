from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # dict1=Counter(nums)
        # print(dict1)
        # count=0
        # for val in dict1.values():
        #     if val>1:
        #         count+=1
        # return count
        operations=0
        while len(nums)>0:
            if len(set(nums))==len(nums):
                break
            nums=nums[3:]
            operations+=1
        return operations