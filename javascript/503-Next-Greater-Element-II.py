class Solution(object):
    def nextGreaterElements(self, nums):
        # n=len(nums)
        # greater=[]
        # for i in range(len(nums)):
        #     next_greater=-1
        #     for j in range(i+1,i+n):
        #         if nums[j%n]>nums[i]:
        #             next_greater=nums[j%n]
        #             break
        #     greater.append(next_greater)
        # return greater
        n=len(nums)
        result=[-1]*n
        stack=[]
        for i in range(2*n):
            while stack and nums[i%n]>nums[stack[-1]]:
                index=stack.pop()
                result[index]=nums[i%n]
            if i<n:
                stack.append(i)
        return result