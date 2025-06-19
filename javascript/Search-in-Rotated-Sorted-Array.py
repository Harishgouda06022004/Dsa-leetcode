class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums=sorted(nums)
        # print(nums)
        n=len(nums)
        # left=0
        # right=n-1
        # while left<right:
        #     mid=(left+right)//2
        #     if nums[mid]==target:
        #         return nums[mid]
        #     elif nums[mid]<target:
        #         left=mid+1
        #     else:
        #         right=mid-1
        # return -1
        # for num in range(0,n):
        #     if nums[num]==target:
        #         return num
        # return -1
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<=target and target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<=target and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1

