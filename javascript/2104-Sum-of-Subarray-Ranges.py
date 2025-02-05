class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total=0
        n=len(nums)
        for i in range(0,n):
            mini=float('inf')
            maxi=float('-inf')
            for j in range(i,n):
                mini=min(mini,nums[j])
                maxi=max(maxi,nums[j])
                ranges=maxi-mini
                total+=ranges
        return total
                