class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # def is_Valid(subset):
        #     for i in range(len(subset)):
        #         for j in range(i):
        #             if subset[i]%subset[j]!=0 and subset[j]%subset[i]!=0:
        #                 return False
        #     return True
        # nums.sort()
        # n=len(nums)
        # max_subset=[]
        # for mask in range(1<<n):
        #     subset=[nums[i] for i in range(n) if mask & (1<<i)]
        #     if is_Valid(subset) and len(subset)>len(max_subset):
        #         max_subset=subset
            
        # return max_subset
        n=len(nums)
        if not nums:
            return []
        nums.sort()
        dp=[1]*n
        prev=[-1]*n
        max_index=0
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    prev[i]=j
            if dp[i]>dp[max_index]:
                max_index=i
        result=[]
        while max_index!=-1:
            result.append(nums[max_index])
            max_index=prev[max_index]
        return result