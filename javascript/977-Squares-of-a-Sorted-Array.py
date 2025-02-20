class Solution(object):
    def sortedSquares(self, nums):
        num=[]
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
            num.append(nums[i])
        return sorted(num)
        