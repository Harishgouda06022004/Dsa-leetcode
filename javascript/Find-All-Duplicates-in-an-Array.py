class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict1={}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        dup=[]
        for key,val in dict1.items():
            if val>1:
                dup.append(key)
        return dup