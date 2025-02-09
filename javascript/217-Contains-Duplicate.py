class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # dict1={}
        # for i in nums:
        #     dict1[i]=dict1.get(i,0)+1
        # for value in dict1.values():
        #     if value>=2:
        #         return True
        # return False
        dict1={}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        print(dict1)
        for value in dict1.values():
            if value>=2:
                return True
        return False
        