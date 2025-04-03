class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # n=len(nums)
        # if n<3:
        #     return 0
        # max_value=0
        # max_i=nums[0]
        # max_k=nums[-1]
        # for j in range(n-2,0,-1):
        #     max_k=max(max_k,nums[j+1])
        #     if max_i>nums[j] and max_k>0:
        #         max_value=max(max_value,(max_i-nums[j])*max_k)
        #     max_i=max(max_i,nums[j])
        # return max_value
        # n = len(nums)
        # if n < 3:
        #     return 0

        # max_i = nums[0]  # Track maximum nums[i] before j
        # min_j = float('inf')  # Track minimum nums[j]
        # max_value = 0  # Store max value of expression

        # for j in range(1, n - 1):  # j should be in the middle
        #     min_j = min(min_j, nums[j])  # Update min_j for nums[j]
            
        #     for k in range(j + 1, n):  # Find valid nums[k] for the triplet
        #         max_value = max(max_value, (max_i - min_j) * nums[k])
            
        #     max_i = max(max_i, nums[j])  # Update max_i after checking j

        # return max_value
        n = len(nums)
        if n < 3:
            return 0
        
        maxBefore = [0] * n
        maxBefore[0] = nums[0]
        for j in range(1, n):
            maxBefore[j] = max(maxBefore[j - 1], nums[j - 1])

        maxAfter = [0] * n
        maxAfter[n - 1] = nums[n - 1]
        for j in range(n - 2, -1, -1):
            maxAfter[j] = max(maxAfter[j + 1], nums[j + 1])

        max_value = 0
        for j in range(1, n - 1):
            max_value = max(max_value, (maxBefore[j] - nums[j]) * maxAfter[j])

        return max_value
