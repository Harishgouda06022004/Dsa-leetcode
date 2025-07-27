class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        prev=nums[0]
        for i in range(0,n-1):
            if nums[i]==nums[i+1]:
                continue
            if prev<nums[i]>nums[i+1] or prev>nums[i]<nums[i+1]:
                count+=1
            prev=nums[i]
        return count