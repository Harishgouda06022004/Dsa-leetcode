class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        n=len(nums)
        high=n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
