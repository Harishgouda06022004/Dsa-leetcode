class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dict1={}
        for n in nums:            
            dict1[n]=dict1.get(n,0)+1
        print(dict1)
        for value in dict1.values():
            if value%2!=0:
                return False
        return True
