from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=Counter(nums)
        arr=[]
        for key,value in s.items():
            if value==2:
                arr.append(key)
        return arr