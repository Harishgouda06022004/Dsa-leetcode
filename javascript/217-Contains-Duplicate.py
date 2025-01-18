class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dict1={}
        for i in nums:
            dict1[i]=dict1.get(i,0)+1
        for value in dict1.values():
            if value>=2:
                return True
        return False
        