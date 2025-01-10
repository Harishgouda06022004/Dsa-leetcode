class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        n=len(nums)
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if target>nums[mid]:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            elif nums[mid]==target:
                return mid
            else:
               return mid
        return -1
        