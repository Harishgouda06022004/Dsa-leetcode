class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1={}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
        print(dict1)
        for key,value in dict1.items():
            if value==1:
                return key