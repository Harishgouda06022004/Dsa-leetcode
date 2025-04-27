class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        # for i in range(n):
        #     for j in range(i+2,n):
        #         if 2*(nums[i]+nums[i+2])==nums[j]:
        #             count+=1
        # return count
        for i in range(n-2):
            if 2*(nums[i]+nums[i+2])==nums[i+1]:
                count+=1
        return count