class Solution(object):
    def sortedSquares(self, nums):
        # num=[]
        # for i in range(len(nums)):
        #     nums[i]=nums[i]*nums[i]
        #     num.append(nums[i])
        # return sorted(num)
        left=0
        right=len(nums)-1
        result=[]
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result.append(nums[left]**2)
                left+=1
            else:
                result.append(nums[right]**2)
                right-=1
        return result[::-1]
        