class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n=len(nums)
        ans=abs(nums[0]-nums[n-1])
        for i in range(n):
            ans=max(ans,abs(nums[i]-nums[i-1]))
        return ans

            