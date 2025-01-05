class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicti={}
        for i in nums:
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i]=1
        for key,value in dicti.items():
            if value==1:
                return key
        return 1
