class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        # for num in nums:
        #     print(nums)
        #     nums_greater=-1
        #     for j in nums:
        #         if nums[j]>nums[num]:
        #             nums_greater=nums[j]
        #     result.append(nums_greater)
        # return result
        # n=len(nums)
        
        # for num in range(0,n):
        #     nums_greater=-1
        #     for j in range(num+1,n):
        #         if nums[j]>nums[num]:
        #             nums_greater=nums[j]
        #             break
        #     result.append(nums_greater)
        # return result
        # n = len(nums)
        # result = [-1] * n  # Initialize result array with -1
        # stack = []  # Monotonic decreasing stack (stores indices)

        # for i in range(n):
        #     while stack and nums[stack[-1]] < nums[i]:
        #         index = stack.pop()  # Pop smaller elements
        #         result[index] = nums[i]  # Update the result for popped index
            
        #     stack.append(i)  # Push current index onto stack

        # return result
        n=len(nums)
        stack=[]
        nge=[2]*n
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
           
            if i<n:
                nge[i]=-1 if not stack else stack[-1]
            stack.append(nums[i%n])
        return nge
        