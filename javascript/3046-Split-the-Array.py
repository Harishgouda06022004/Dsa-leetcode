class Solution(object):
    def isPossibleToSplit(self, nums):
        dict1={}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        print(dict1)
        for value in dict1.values():
            if value>2:
                return False
        return True
        