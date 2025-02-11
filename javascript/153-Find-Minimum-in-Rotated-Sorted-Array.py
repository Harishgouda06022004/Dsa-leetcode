class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        n=len(nums)
        low=0
        high=n-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans