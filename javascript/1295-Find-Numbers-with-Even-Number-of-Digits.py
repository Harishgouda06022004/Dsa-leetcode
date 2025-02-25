class Solution(object):
    def findNumbers(self, nums):
        count=0
        for num in nums:
            # for i in str(num):
            #     if len(i)%2==0:
            #         count+=1
            if len(str(num))%2==0:
                count+=1
        return count
        