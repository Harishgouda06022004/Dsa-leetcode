class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        # for num in range(0,n):
        #     if nums[num]==target:
        #         return True
        # return False
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low=low+1
                high=high-1
                continue

            if nums[low]<=nums[mid]:
                if nums[low]<=target and target<=nums[mid]:
                        high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
                