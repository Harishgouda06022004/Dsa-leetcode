class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        return max(dict1,key=dict1.get)


