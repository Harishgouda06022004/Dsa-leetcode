class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1={}
        for key in nums:
            dict1[key]=dict1.get(key,0)+1
        for key,value in dict1.items():
            if value==1:
                return key
        return 0