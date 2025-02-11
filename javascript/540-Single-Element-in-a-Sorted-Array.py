from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dict1={}
        count=Counter(nums)
        print(count)
        # return next(key for key,value in count.items() if value==1)
        for key,value in count.items():
            if value==1:
                return key
        
        