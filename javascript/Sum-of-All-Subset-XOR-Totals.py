class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # total=0
        # n=len(nums)
        # for mask in range(1<<n):
        #     xor_total=0
        #     for i in range(n):
        #         if mask & (1<<i):
        #             xor_total^=nums[i]
        #     total+=xor_total
        # return total
        # def dfs(i,total):
        #     if i==len(nums):
        #         return total
        #     return dfs(i+1,total^nums[i])+dfs(i+1,total)
        # return dfs(0,0)
        res=0
        for n in nums:
            res |=n
        return res*2**(len(nums)-1)